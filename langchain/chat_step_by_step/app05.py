"""
Goal: AI to help customer find best present for their loved ones.
05 - Proper function call (OpenAI finetuned spec) to get real catalog.
"""

from langchain.chat_models import AzureChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.prompts import SystemMessagePromptTemplate, ChatPromptTemplate
from langchain.pydantic_v1 import BaseModel, Field
from langchain.chains.openai_functions import create_openai_fn_chain
import gradio as gr
import os
import templates
import json

# Get access credentials
BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("API_KEY")
DEPLOYMENT_NAME = os.getenv("DEPLOYMENT_NAME")

# Create chat model
llm = AzureChatOpenAI(
    openai_api_base=BASE_URL,
    openai_api_version="2023-07-01-preview",
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
    history_langchain_format.append(SystemMessagePromptTemplate.from_template(templates.system_message_template05))

    # Get conversation history from Gradio and add message to list
    for human, ai in history:
        history_langchain_format.append(HumanMessage(content=human))
        history_langchain_format.append(AIMessage(content=ai))

    # Add latest user message to list
    history_langchain_format.append(HumanMessage(content=message))

    # Apply inputs to template
    chat_prompt = ChatPromptTemplate.from_messages(history_langchain_format).format_prompt(user_info=user_info_example).to_messages()
    chat_prompt_template = ChatPromptTemplate.from_messages(history_langchain_format)

    # Get response from AI
    print("***********************************")
    chain = create_openai_fn_chain([RequestCatalogItems], llm, chat_prompt_template, verbose=False)
    # chain.llm_kwargs["function_call"] = "auto"
    print(chain.to_json)
    gpt_response = chain(inputs = {"user_info":user_info_example})
    print(f"AI: {gpt_response}")

    # # Check if function has been called
    # if "SHOW_CATEGORY" in gpt_response.content:
    #     print("Function has been called, getting items from catalog...")

    #     # Get items from catalog from category user has selected and create new prompt
    #     items_prompt = f"Here are catalog items in JSON, please parse it and show it to user: {get_catalog(category='robot')}"
        
    #     # Add this prompt as human message to history
    #     history_langchain_format.append(HumanMessage(content=items_prompt))
    #     chat_prompt = ChatPromptTemplate.from_messages(history_langchain_format).format_prompt(user_info=user_info_example).to_messages()
        
    #     # Get response from AI and respond with this one
    #     gpt_response = llm(chat_prompt)
    #     print(f"NEW AI: {gpt_response.content}")
    return gpt_response.content

# Function call class
class RequestCatalogItems(BaseModel):
    """Getting items on stock for category."""

    category: str = Field(..., description="Category of presents to show")

class Dummy(BaseModel):
    """Do not use."""

    category: str = Field(..., description="Category of presents to show")

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