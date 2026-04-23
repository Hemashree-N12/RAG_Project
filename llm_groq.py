import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()  # loads GROQ_API_KEY from .env

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_groq(question, context=""):
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",   
        messages=[
            {"role": "system", "content": "You are a helpful customer support assistant."},
            {"role": "user", "content": f"Answer using this context:\n{context}\n\nQuestion: {question}"}
        ],
        temperature=0
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    q = input("Ask: ")
    print(ask_groq(q))
