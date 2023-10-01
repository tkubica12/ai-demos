"""
Goal: AI to help customer find best present for their loved ones.
02 - Try to limit model to not offer categories that are not listed.

Note that for GPT 3.5 you need to do more work to make it stop offering different categories (repeat instruction on end so due to repetition and recency bias model behaves as expected). With GPT 4 just single sentence is enough to ensure the same.

This shows that how well model follows instructions is dependent on model size as well as any instruction tuning that has been done.
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

**Do not offer categories that are not listed.**
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