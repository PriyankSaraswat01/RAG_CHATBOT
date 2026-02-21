from fastapi import APIRouter
from app.schemas.chat_schema import ChatRequest, ChatResponse
from app.services.rag_chain import get_rag_chain

router = APIRouter()

rag_chain = get_rag_chain()

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    response = rag_chain.invoke(request.question)
    return ChatResponse(answer=response)