def escalate_to_human(question, context):
    print("\n--- HUMAN ESCALATION REQUIRED ---")
    print("Question:", question)
    print("Context:", context)
    print("Please provide a manual answer here.\n")

if __name__ == "__main__":
    escalate_to_human("What is the refund policy?", "No confident AI answer found.")