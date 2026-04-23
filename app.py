import streamlit as st
from workflow import workflow
from query import run_query

st.set_page_config(page_title="Customer Support Assistant", page_icon="💬")

st.title("📚 Customer Support Assistant (RAG + HITL)")

user_query = st.text_input("Ask a question:")

if st.button("Submit"):
    try:
        context, confidence = run_query(user_query)
        answer = workflow(user_query)

        # Show answer differently depending on HITL vs Groq
        if "HITL" in answer:
            st.error(answer)  # Red box for escalation
        else:
            st.success(answer)  # Green box for valid answers

        # Show debug info for demo transparency
        with st.expander("🔍 Retrieved Context & Confidence"):
            st.write("**Confidence Score:**", confidence)
            st.write("**Context Used:**")
            st.text(context if context else "No context retrieved")

    except Exception as e:
        st.error(f"Error: {e}")
