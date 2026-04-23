from llm_groq import answer_with_llm
from hitl import escalate_to_human

def workflow(question):
    try:
        answer = answer_with_llm(question)
        if not answer or "i don't know" in answer.lower():
            escalate_to_human(question, "Low confidence from Groq")
        else:
            print("AI Answer:\n", answer)
    except Exception as e:
        print("Error in workflow:", e)

if __name__ == "__main__":
    while True:
        q = input("Workflow question: ")
        if q.lower() in ["exit", "quit"]:
            break
        workflow(q)