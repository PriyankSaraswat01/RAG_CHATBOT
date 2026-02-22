# 📚 RAG Chatbot – Document-Based AI Assistant

A Retrieval-Augmented Generation (RAG) chatbot built using **LangChain**, **FAISS**, **OpenAI LLM**, and **FastAPI**.  
The system answers questions strictly from a connected PDF document.

---

## 🚀 Features

- 🔍 Semantic Search using FAISS
- 🧠 OpenAI GPT-based LLM for response generation
- 📄 PDF ingestion and chunking pipeline
- 📦 Modular project architecture
- ⚡ FastAPI backend with Swagger UI
- 🛡 Strict document-grounded answering
- 🔄 Custom retrieval tuning (similarity search)
- 🧪 Debug mode for retrieved chunks

---

## 🏗 Architecture

User Query  
⬇  
Retriever (FAISS + Embeddings)  
⬇  
Relevant Document Chunks  
⬇  
Prompt Template (Strict Grounding)  
⬇  
OpenAI LLM  
⬇  
Final Answer  

---

## 📂 Project Structure

rag-chatbot/
│
├── app/
│ ├── api/
│ │ └── routes.py
│ ├── core/
│ │ └── config.py
│ ├── services/
│ │ ├── loader.py
│ │ ├── embedding_model.py
│ │ ├── vector_store.py
│ │ ├── retriever.py
│ │ ├── llm.py
│ │ └── rag_chain.py
│ └── main.py
│
├── data/
│ └── main_notes.pdf
│
├── scripts/
│ ├── ingest.py
│ └── check_pdf.py
│
├── vector_db/
├── .env
├── .gitignore
└── README.md

