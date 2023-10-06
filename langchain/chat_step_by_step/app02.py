"""
Goal: AI to help customer find best present for their loved ones.
02 - Try to limit model to not offer categories that are not listed.
"""

from langchain.chat_models import AzureChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
import gradio as gr
import os
import templates

# Get access credentials
BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("API_KEY")
DEPLOYMENT_NAME = os.getenv("DEPLOYMENT_NAME")

# Create chat model
llm = AzureChatOpenAI(
    openai_api_base=BASE_URL,
    openai_api_version="2023-05-15",
    deployment_name=DEPLOYMENT_NAME,
    openai_api_key=API_KEY,
    openai_api_type="azure",
)

# Get chat response from AI
def chat(message, history):

    # Log user message
    print(f"User: {message}")

    # Build list of messages
    history_langchain_format = []

    # Add system message
    history_langchain_format.append(SystemMessage(content = templates.system_message_template02))

    # Get conversation history from Gradio and add message to list
    for human, ai in history:
        history_langchain_format.append(HumanMessage(content=human))
        history_langchain_format.append(AIMessage(content=ai))

    # Add latest user message to list
    history_langchain_format.append(HumanMessage(content=message))

    # Get response from AI
    gpt_response = llm(history_langchain_format)
    print(f"AI: {gpt_response.content}")
    return gpt_response.content

# Run main chat user interface
gr.ChatInterface(chat).launch()