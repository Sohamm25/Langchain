from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
import os
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","hi please answer to these questions in short"),
        ("user","Question:{question}")
    ]
)
import streamlit as st
st.title("HI this chatbot(openai) is made by Soham, search the topic u want and u will get the answer!")
input_text=st.text_input("Search!")
#down below will be changed when using llama2
llm=ChatOpenAI(model="gpt-3.5-turbo")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser
if input_text:
    st.write(chain.invoke({'question':input_text}))
