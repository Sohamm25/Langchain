from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","please respond to these questions in short"),
        ("user","Question:{question}")
    ]
)
st.title("HI this chatbot(LOCAL LLM OLLAMA) is made by Soham, search the topic u want and u will get the answer!")
input_text=st.text_input("Search!")
#this is local llm
llm=Ollama(model="llama2")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser
if input_text:
    st.write(chain.invoke({"question":input_text}))
