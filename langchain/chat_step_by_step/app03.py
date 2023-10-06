"""
Goal: AI to help customer find best present for their loved ones.
03 - Simulate loading user information from external system such as Feature Store.
"""

from langchain.chat_models import AzureChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.prompts import SystemMessagePromptTemplate, ChatPromptTemplate
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

# Example user information (this should be loaded from external system based on logged in user)
user_info_example = """
- Person: Jane, daughter, 5
- Person: Thomas, son, 2
- Person: Justine, wife, 38
- Recommendations: Toy robot, Flowers
"""

# Get chat response from AI
def chat(message, history):

    # Log user message
    print(f"User: {message}")

    # Build list of messages
    history_langchain_format = []

    # Add system message template
    history_langchain_format.append(SystemMessagePromptTemplate.from_template(templates.system_message_template03))

    # Get conversation history from Gradio and add message to list
    for human, ai in history:
        history_langchain_format.append(HumanMessage(content=human))
        history_langchain_format.append(AIMessage(content=ai))

    # Add latest user message to list
    history_langchain_format.append(HumanMessage(content=message))

    # Apply inputs to template
    chat_prompt = ChatPromptTemplate.from_messages(history_langchain_format).format_prompt(user_info=user_info_example).to_messages()

    # Get response from AI
    gpt_response = llm(chat_prompt)
    print(f"AI: {gpt_response.content}")
    return gpt_response.content

# Run main chat user interface
gr.ChatInterface(chat).launch()