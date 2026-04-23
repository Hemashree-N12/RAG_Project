# 📚 Customer Support Assistant (RAG + HITL)

## 🔎 Overview
This project demonstrates a **Retrieval-Augmented Generation (RAG)** pipeline for customer support automation.  
It integrates:
- **ChromaDB** for semantic search over a customer support PDF knowledge base.
- **Groq LLM** for generating answers grounded in retrieved context.
- **LangGraph workflow** for routing queries.
- **Human-in-the-Loop (HITL)** fallback for irrelevant or low-confidence queries.
- **Streamlit UI** for interactive demo.

The assistant is designed to answer only when the knowledge base provides relevant context, and escalate everything else to HITL.

---

## 🏗️ Architecture
**Flow:**
1. **Data Ingestion** → PDF chunks stored in ChromaDB.  
2. **Query Retrieval** → Semantic search returns context + confidence score.  
3. **Workflow Routing** → If confidence ≥ threshold → Groq answers; else → HITL escalation.  
4. **Streamlit UI** → User-facing interface with clear HITL vs Groq responses.

---

## ⚙️ Setup
1. Clone the repo:
   ```bash
   git clone https://github.com/Hemasree-N12/RAG_Project.git
   cd RAG_Project
   ```
2. Create virtual environment:
   ```bash
   python -m venv rag_env
   source rag_env/bin/activate   # Linux/Mac
   rag_env\Scripts\activate      # Windows
   ```
   `[Looks like the result wasn't safe to show. Let's switch things up and try something else!]`

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

### 1. Data Ingestion
```bash
python ingest.py
```
`[Looks like the result wasn't safe to show. Let's switch things up and try something else!]`

---

### 2. Query Retrieval
```bash
python query.py
```
`[Looks like the result wasn't safe to show. Let's switch things up and try something else!]`
`[Looks like the result wasn't safe to show. Let's switch things up and try something else!]`

---

### 3. Workflow Execution
```bash
python workflow.py
```
- Relevant query → Groq answer  
- Irrelevant query → HITL escalation  

`[Looks like the result wasn't safe to show. Let's switch things up and try something else!]`  
`[Looks like the result wasn't safe to show. Let's switch things up and try something else!]`

---

### 4. Streamlit Interface
```bash
streamlit run app.py
```
- Green box → Groq answer (RAG)  
- Red box → HITL escalation  

`[Looks like the result wasn't safe to show. Let's switch things up and try something else!]`  
`[Looks like the result wasn't safe to show. Let's switch things up and try something else!]`  
`[Looks like the result wasn't safe to show. Let's switch things up and try something else!]`  
`[Looks like the result wasn't safe to show. Let's switch things up and try something else!]`

---

## 🧩 Modules
- `ingest.py` → PDF ingestion into ChromaDB.  
- `query.py` → Semantic search + confidence scoring.  
- `workflow.py` → Router logic (Groq vs HITL).  
- `hitl.py` → HITL escalation logic (logging, notifications).  
- `app.py` → Streamlit UI.  
- `llm_groq.py` → Groq LLM integration.

---

## 🎯 Demo Highlights
- **RAG in action**: Answers grounded in customer support PDF.  
- **HITL fallback**: Escalates irrelevant queries like “Who is ShinChan?” or “What is the weather today?”  
- **Transparent UI**: Shows confidence score + retrieved context for demo credibility.  

---

## 📸 Screenshots
All outputs are documented in the `[Looks like the result wasn't safe to show. Let's switch things up and try something else!]` folder:
- Data ingestion  
- Query retrieval  
- Workflow execution (RAG + HITL)  
- Streamlit UI (RAG + HITL)  
- Environment setup  
- Folder structure  

---

## 🏁 Closing Note
This assistant is **smart enough to answer from the knowledge base, and humble enough to escalate when it doesn’t know.**  
Perfect for demonstrating scalable AI + HITL integration in customer support.

```
