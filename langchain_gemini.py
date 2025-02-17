!pip install langchain_core
!pip install langchain_google_genai
!pip install python-dotenv
!pip install streamlit

import getpass
import os
import streamlit
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


GOOGLE_API_KEY= "AIzaSyDMdPhM5dj5OG95kfF2hsSUq4j1w7IXz9k"
LANGCHAIN_API_KEY = "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"
LANGCHAIN_PROJECT = "playground"


os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
os.environ["LANGCHAIN_API_KEY"] = LANGCHAIN_API_KEY
os.environ["LANGCHAIN_PROJECT"] = LANGCHAIN_PROJECT

llm = ChatGoogleGenerativeAI(
    model = "gemini-1.5-pro",
    temperature = 0,
    max_tokens = 1000,
    timeout = None,
    max_retires = 2
)


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a CHatbot!"),
        ("human", "Question: {question}")
    ]
)

outputparser = StrOutputParser()

chain = prompt|llm|outputparser

question ="What is Streamlit and put some commands for inbox, checkbox and other 20 commands for input and outputs?"


a = chain.invoke({"question" : question})

print(a)

