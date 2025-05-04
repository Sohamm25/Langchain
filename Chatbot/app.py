from langchain_openai import ChatOpenai
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
from dotenv import load_dotenv
import os
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
#tracked by langsmith
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

abc=ChatPromptTemplate.from_messages(
[
    ("system", "You are a helpful assistant. Please response to the user queries"),
    ("user", "Question:{question}")
]
)
st.title("HI this chatbot(OPENAI) is made by Soham, search the topic u want and u will get the answer!")
input_by_user = st.text_input("Search!")
llm=ChatOpenai(model="gpt-3.5-turbo")
output_parser=StrOutputParser(),
chain=abc | llm | output_parser
if st.input_by_user:
    st.write(chain.invoke({"question": input_by_user})) 
