"""
Goal: AI to help customer find best present for their loved ones.
05 - Proper function call (OpenAI finetuned spec) to get real catalog.
"""

import openai
import os
import gradio as gr
import pprint
import json
from string import Template
import re

# Set OpenAI API credentials
openai.api_type = "azure"
openai.api_key = os.getenv("API_KEY")
openai.api_base = os.getenv("BASE_URL")
openai.api_version = "2023-07-01-preview"
deployment_name = os.getenv("DEPLOYMENT_NAME")

# Define prompt
system_message_template = """
You are shopping assistant for online retailer and your task is to help users find best present for their loved ones. Do NOT offer other categories of presents than those listed below. 

Here are typical presents for different audiences:
- small boy -> toy car, toy train, toy robot
- small girl -> doll, toy house, toy kitchen
- adolescent boy -> computer game, computer, bicycle
- adolescent girl -> cosmetics, clothes, jewelry
- adult woman -> jewelry, theater tickets, flowers
- adult man -> gadgets, wine, restaurant vouchers
- elderly -> lottery ticket, book, liquor

If you are asked for present in category that is not listed above, explain politely our store does not offer those and offer something else from list above. 

Example:
User: I am looking for present for my 5 years old son. Toy gun.
Assistant: I am sorry, we are not offering toy guns. I can offer you toy car, toy train or toy robot. Would you like to see some of them?

Here are information from our database about connected customer. Use it to help user find the best present, offer them choices based on this information. As you are referring to this information do not use definitive language. For example instead of "You have 2 children" say "You have 2 children, right?". Instead of "You have a boy" use "Our records indicate you have a boy, is it correct? Are you looking for present for him?".

User information: $user_info

**Do not offer categories that are not listed.**

Do not make up options, rather use SHOW_CATEGORY function as described below.

When user agree to see offered product category or ask for options you **MUST** use show_category function.

After this you will get response with JSON with items in this category as user message. You should parse this JSON and show it to user in nice form.

Example response from show_category:
[{"name": "MyItem", "price": 10, "description": "MyItem is nice and affordable."}]

Example output you should create after parsing response:
1. MyItem for 10 USD - great if you are looking for something nice and affordable
"""

# Example user information (this should be loaded from external system based on logged in user)
user_info_example = """
- Person: Jane, daughter, 5
- Person: Thomas, son, 2
- Person: Justine, wife, 38
- Recommendations: Toy robot, Flowers
"""

# Define OpenAI function
functions = [
    {
        "name": "show_category",
        "description": "Get items from catalog for category user has selected",
        "parameters": {
            "type": "object",
            "properties": {
                "category": {
                    "type": "string",
                    "enum": ["toy_car", "toy_train", "toy_robot", "doll", "toy_house", "toy_kitchen", "computer_game", "computer", "bicycle", "cosmetics", "clothes", "jewelry", "jewelry", "theater_tickets", "flowers", "gadgets", "wine", "restaurant_vouchers", "lottery_ticket", "book", "liquor"],
                    "description": "Category user has selected.",
                },
            },
            "required": ["location", "format"],
        },
    },
]

# Get response from AI
def chat(message, history):

    # Build list of messages
    messages = []

    # Create empty messages
    system_message = {}
    user_message = {}
    assistant_message = {}

    # Add system message
    system_message["role"] = "system"
    system_message["content"] = Template(system_message_template).substitute(user_info=user_info_example)
    messages.append(system_message)

    # Get conversation history from Gradio and add message to list
    for user, assistant in history:
        user_message["role"] = "user"
        user_message["content"] = user
        messages.append(user_message)

        assistant_message["role"] = "assistant"
        assistant_message["content"] = assistant
        messages.append(assistant_message)

    # Add latest user message to list
    user_message["role"] = "user"
    user_message["content"] = message
    messages.append(user_message)

    # Get response from AI
    print(f"\n\n*** Messages ***\n\n{json.dumps(messages, indent=2)}\n\n") # Log request
    response = openai.ChatCompletion.create(deployment_id=deployment_name, model="gpt-4", messages=messages, functions=functions)
    print(f"\n\n*** Response ***\n\n{response.choices[0]}\n\n") # Log response

    # Decide what to do whether response contains function call or just content
    if hasattr(response.choices[0].message, "function_call"):
        if response.choices[0].message["function_call"]["name"] == "show_category":
            # Get category from function call
            arguments = json.loads(response.choices[0].message["function_call"]["arguments"])
            category = arguments["category"]
            print(f"Function has been called, getting items from {category}.")
            
            # Get items from catalog from category user has selected and create new prompt
            items_prompt = f"Here are catalog items in JSON, please parse it and show it to user: {get_catalog(category=category)}"
            
            # Add this prompt
            items_message = {}
            items_message["role"] = "system"
            items_message["content"] = items_prompt
            messages.append(items_message)

            # Get response from AI
            print(f"\n\n*** Messages ***\n\n{json.dumps(messages, indent=2)}\n\n") # Log request
            response = openai.ChatCompletion.create(deployment_id=deployment_name, model="gpt-4", messages=messages, functions=functions)
            print(f"\n\n*** Response ***\n\n{response.choices[0]}\n\n") # Log response
            response_message = response.choices[0].message.content
    else:
        response_message = response.choices[0].message.content


    # # Check if function has been called
    # if "SHOW_CATEGORY" in response_message:
    #     # Define regular expression pattern to match category name
    #     pattern = r"SHOW_CATEGORY\((\w+)\)"

    #     # Use regular expression to extract category name from response_message
    #     category = re.search(pattern, response_message)
    #     print(f"Function has been called, getting items from {category}.")

    #     # Get items from catalog from category user has selected and create new prompt
    #     items_prompt = f"Here are catalog items in JSON, please parse it and show it to user: {get_catalog(category=category)}"
        
    #     # Add this prompt
    #     items_message = {}
    #     items_message["role"] = "system"
    #     items_message["content"] = items_prompt
    #     messages.append(items_message)

    #     # Get response from AI
    #     print(f"\n\n*** Messages ***\n\n{json.dumps(messages, indent=2)}\n\n") # Log request
    #     response = openai.ChatCompletion.create(deployment_id=deployment_name, model="gpt-4", messages=messages)
    #     print(f"\n\n*** Response ***\n\n{response.choices[0]}\n\n") # Log response
    #     response_message = response.choices[0].message.content

    return response_message

# Function that is simulating getting items from catalog
def get_catalog(category: str) -> str:
    print(f"Getting items from catalog for category: {category}")
    items = [
        {"name": "Super robot", "price": 50, "description": "This is a super robot toy"},
        {"name": "Basic robot", "price": 20, "description": "Very good robot with basic functions"},
        {"name": "Robot deluxe", "price": 90, "description": "Luxury robot with advanced features"}
    ] # We have hardcoded one example, but this should be loaded from external system
    return json.dumps(items)

# Run main chat user interface
gr.ChatInterface(chat).launch()