from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="RAG Chatbot API")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "RAG Chatbot is running 🚀"}