from langchain_community.document_loaders import PyPDFLoader
from app.core.config import settings

def load_documents():
    loader = PyPDFLoader(settings.DATA_PATH)
    documents = loader.load()
    return documents