import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

def ingest_pdf(pdf_path="database/knowledge_base.pdf", persist_dir="chroma_store"):
    if not os.path.exists(pdf_path):
        print(f"❌ PDF not found at {pdf_path}. Place your file here first.")
        return

    print(f"📥 Loading PDF: {pdf_path}")
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(documents)

    print(f"🔢 Created {len(chunks)} chunks. Generating embeddings...")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = Chroma.from_documents(chunks, embeddings, persist_directory=persist_dir)
    db.persist()

    print(f"✅ Ingested {len(chunks)} chunks into {persist_dir}")

if __name__ == "__main__":
    ingest_pdf()