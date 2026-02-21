from langchain_community.vectorstores import FAISS
from app.core.config import settings

def create_vector_store(chunks, embeddings):
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(settings.VECTOR_DB_PATH)
    return vectorstore


def load_vector_store(embeddings):
    vectorstore = FAISS.load_local(
        settings.VECTOR_DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )
    return vectorstore