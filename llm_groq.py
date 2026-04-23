import os
from dotenv import load_dotenv
from groq import Groq
from query import query_db

load_dotenv()

def answer_with_llm(question):
    results = query_db(question)
    context = "\n".join([r.page_content for r in results])

    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "You are a helpful customer support assistant."},
            {"role": "user", "content": f"Answer using this context:\n{context}\n\nQuestion: {question}"}
        ],
        temperature=0
    )
    return response.choices[0].message.content