# from app.services.embedding_model import get_embedding_model
# from app.services.vector_store import load_vector_store

# def get_retriever():
#     embeddings = get_embedding_model()
#     vectorstore = load_vector_store(embeddings)

#     retriever = vectorstore.as_retriever(
#         search_kwargs={"k": 3}
#     )

#     return retriever



from app.services.embedding_model import get_embedding_model
from app.services.vector_store import load_vector_store

def get_retriever():
    embeddings = get_embedding_model()
    vectorstore = load_vector_store(embeddings)

    retriever = vectorstore.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={
            "score_threshold": 0.5,  # Adjust if needed
            "k": 3
        }
    )

    return retriever