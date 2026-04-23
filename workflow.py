from llm_groq import ask_groq
from query import run_query

def router_node(state):
    query_terms = state["query"].lower().split()
    context_text = state.get("context", "").lower()

    # Require at least 2 query terms to appear in context
    relevance_hits = sum(1 for term in query_terms if term in context_text)

    if state.get("confidence", 0.0) >= 0.7 and relevance_hits >= 2:
        return "answer_node"
    else:
        return "hitl_node"

def answer_node(state):
    return {"answer": ask_groq(state["query"], state.get("context", ""))}

def hitl_node(state):
    return {"answer": "Escalated to human agent (HITL)."}

def workflow(query):
    context, confidence = run_query(query)
    state = {"query": query, "context": context, "confidence": confidence}

    next_node = router_node(state)
    if next_node == "answer_node":
        result = answer_node(state)
    else:
        result = hitl_node(state)

    return result["answer"]

if __name__ == "__main__":
    q = input("Workflow question: ")
    print(workflow(q))
