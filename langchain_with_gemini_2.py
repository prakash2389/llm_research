import getpass
import os
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

llm = ChatGoogleGenerativeAI(
    model = "gemini-1.5-pro",
    temperature = 0,
    max_tokens = 1000,
    timeout = None,
    max_retires = 2
)


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a Chatbot! You will be translating the below human response from {input_language} to {output_language}"),
        ("human", "Question: {question}")
    ]
)

outputparser = StrOutputParser()

chain = prompt|llm|outputparser

# question ="WHat is Streamlit and put some commands for inbox, checkbox and other 20 commands for input and outputs?"


st.title("Langchian_with Gemini")
input_text = st.text_input("Enter your question here:")
input_language = st.text_input("Enter input_language:")
output_language = st.text_input("Enter output_language:")


if input_text and input_language and output_language:
    st.write(chain.invoke({
    "input_language" : input_language,
    "output_language" : output_language,
    "question" : input_text}))

