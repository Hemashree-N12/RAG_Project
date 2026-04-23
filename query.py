import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

persist_dir = "chroma_store"

# Initialize embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Load the Chroma database
db = Chroma(persist_directory=persist_dir, embedding_function=embeddings)

def run_query(query: str):
    """
    Run a semantic search query against the Chroma database.
    Returns: (context, confidence)
    """
    results = db.similarity_search_with_score(query, k=3)

    # Build context from top results
    context = "\n".join([doc.page_content for doc, _ in results])

    if results:
        scores = [score for _, score in results]
        avg_score = sum(scores) / len(scores)
        confidence = max(0.0, 1.0 - avg_score / 50.0)
    else:
        confidence = 0.0

    return context, confidence

if __name__ == "__main__":
    q = input("Enter your query: ")
    context, confidence = run_query(q)
    print("Context:\n", context)
    print("Confidence:", confidence)
