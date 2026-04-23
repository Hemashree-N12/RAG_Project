from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

def query_db(question, persist_dir="chroma_store"):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = Chroma(persist_directory=persist_dir, embedding_function=embeddings)
    results = db.similarity_search(question, k=3)
    return results

if __name__ == "__main__":
    while True:
        q = input("Ask a question: ")
        if q.lower() in ["exit", "quit"]:
            break
        answers = query_db(q)
        for i, ans in enumerate(answers, 1):
            print(f"\nResult {i}:\n{ans.page_content}\n")