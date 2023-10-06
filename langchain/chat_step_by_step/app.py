"""
Test
"""

from langchain.chat_models import AzureChatOpenAI
from langchain.chains import TransformChain, LLMChain, SimpleSequentialChain
from langchain.schema import AIMessage, HumanMessage
from langchain.prompts import SystemMessagePromptTemplate, ChatPromptTemplate
import openai
import gradio as gr
import os
import templates

BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("API_KEY")
DEPLOYMENT_NAME = "gpt-35-turbo"

llm = AzureChatOpenAI(
    openai_api_base=BASE_URL,
    openai_api_version="2023-05-15",
    deployment_name=DEPLOYMENT_NAME,
    openai_api_key=API_KEY,
    openai_api_type="azure",
)

user_info_example = """
- Jane, daughter, 5
- Thomas, son, 2
- Justine, wife, 38
"""

def predict(message, history):
    history_langchain_format = []
    history_langchain_format.append(SystemMessagePromptTemplate.from_template(templates.system_message_template))
    for human, ai in history:
        history_langchain_format.append(HumanMessage(content=human))
        history_langchain_format.append(AIMessage(content=ai))
    history_langchain_format.append(HumanMessage(content=message))
    chat_prompt = ChatPromptTemplate.from_messages(history_langchain_format)
    chat_prompt = chat_prompt.format_prompt(user_info=user_info_example).to_messages()
    gpt_response = llm(chat_prompt)
    print(gpt_response.content)
    return gpt_response.content

gr.ChatInterface(predict).launch()