import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME = "RAG Chatbot"
    
    DATA_PATH = "data/main_notes.pdf"
    VECTOR_DB_PATH = "vector_db/"
    
    CHUNK_SIZE = 1000
    CHUNK_OVERLAP = 200
    
    EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

settings = Settings()