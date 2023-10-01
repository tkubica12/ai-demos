"""
Goal: AI to help customer find best present for their loved ones.
01 - Basic chat with simple prompt with categories of presents.
"""

import openai
import os
import gradio as gr
import pprint
import json

# Set OpenAI API credentials
openai.api_type = "azure"
openai.api_key = os.getenv("API_KEY")
openai.api_base = os.getenv("BASE_URL")
openai.api_version = "2023-07-01-preview"
deployment_name = os.getenv("DEPLOYMENT_NAME")

# Define prompt
system_message_template = """
You are shopping assistant for online retailer and your task is to help users find best present for their loved ones. 

Here are typical presents for different audiences:
- small boy -> toy car, toy train, toy robot
- small girl -> doll, toy house, toy kitchen
- adolescent boy -> computer game, computer, bicycle
- adolescent girl -> cosmetics, clothes, jewelry
- adult woman -> jewelry, theater tickets, flowers
- adult man -> gadgets, wine, restaurant vouchers
- elderly -> lottery ticket, book, liquor
"""

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
    system_message["content"] = system_message_template
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
    response = openai.ChatCompletion.create(deployment_id=deployment_name, model="gpt-4", messages=messages)
    print(f"\n\n*** Response ***\n\n{response.choices[0]}\n\n") # Log response
    response_message = response.choices[0].message.content
    return response_message

# Run main chat user interface
gr.ChatInterface(chat).launch()