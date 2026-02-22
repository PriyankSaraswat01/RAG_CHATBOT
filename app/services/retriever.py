# from app.services.embedding_model import get_embedding_model
# from app.services.vector_store import load_vector_store

# def get_retriever():
#     embeddings = get_embedding_model()
#     vectorstore = load_vector_store(embeddings)

#     retriever = vectorstore.as_retriever(
#         search_kwargs={"k": 3}
#     )

#     return retriever



# from app.services.embedding_model import get_embedding_model
# from app.services.vector_store import load_vector_store

# def get_retriever():
#     embeddings = get_embedding_model()
#     vectorstore = load_vector_store(embeddings)

#     retriever = vectorstore.as_retriever(
#         search_type="mmr",
#         search_kwargs={"k": 3, "fetch_k": 10, "lambda_mult": 0.5}
#     )

#     return retriever



from app.services.embedding_model import get_embedding_model
from app.services.vector_store import load_vector_store

def get_retriever():
    embeddings = get_embedding_model()
    vectorstore = load_vector_store(embeddings)

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 8}
    )

    return retriever

