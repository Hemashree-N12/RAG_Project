import streamlit as st
from workflow import workflow

st.title("Customer Support RAG Assistant (Groq AI)")

question = st.text_input("Ask a question:")
if st.button("Submit"):
    st.write("Answer:")
    workflow(question)