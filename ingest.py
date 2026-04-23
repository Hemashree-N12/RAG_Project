import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

def ingest_pdf():
    pdf_path = "database/knowledge_base.pdf"
    print(f"📥 Loading PDF: {pdf_path}")

    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    # Split into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = text_splitter.split_documents(documents)
    print(f"🔢 Created {len(docs)} chunks. Generating embeddings...")

    # Initialize embeddings
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Create Chroma DB (persistent)
    persist_dir = "chroma_store"
    db = Chroma.from_documents(docs, embeddings, persist_directory=persist_dir)

    print("✅ Ingestion complete. Embeddings stored in ChromaDB.")

if __name__ == "__main__":
    ingest_pdf()
