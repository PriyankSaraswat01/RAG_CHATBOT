from app.services.loader import load_documents
from app.services.chunker import split_documents
from app.services.embedding_model import get_embedding_model
from app.services.vector_store import create_vector_store

def run_ingestion():
    print("Loading documents...")
    documents = load_documents()
    
    print("Splitting documents...")
    chunks = split_documents(documents)
    
    print("Loading embedding model...")
    embeddings = get_embedding_model()
    
    print("Creating vector store...")
    create_vector_store(chunks, embeddings)
    
    print("Ingestion completed successfully!")

if __name__ == "__main__":
    run_ingestion()