from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
from dotenv import load_dotenv
import streamlit as st
load_dotenv()
import os
#THIS IS BEING TRACKED BY LANGSMITH
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
abc = ChatPromptTemplate.from_messages(
[
    ("system", "Hi please answer these questions."),
    ("user", "Question:{question}")
]
)
st.title("HI this chatbot(LOCAL LLM OLLAMA) is made by Soham, search the topic u want and u will get the answer!")
input_by_user = st.text_input("Search!")
llm = Ollama(model="llama2-uncensored")
output_parser = StrOutputParser()
chain = abc | llm | output_parser
if input_by_user:
    st.write(chain.invoke({"question": input_by_user}))
