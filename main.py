import os
from dotenv import load_dotenv
from ingest import ingest_pdf
from workflow import workflow

load_dotenv()

def run_pipeline():
    print("🚀 Starting Customer Support RAG Assistant (Groq AI)")

    pdf_path = "database/knowledge_base.pdf"
    if os.path.exists(pdf_path):
        print("📥 Found PDF, ingesting...")
        ingest_pdf(pdf_path)
    else:
        print("⚠️ No PDF found yet. You can add it later as database/knowledge_base.pdf")

    while True:
        q = input("\nAsk a question (or type 'exit' to quit): ")
        if q.lower() in ["exit", "quit"]:
            print("👋 Exiting assistant.")
            break
        workflow(q)

if __name__ == "__main__":
    run_pipeline()