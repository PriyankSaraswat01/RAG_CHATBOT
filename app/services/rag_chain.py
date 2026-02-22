# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.runnables import RunnablePassthrough
# from langchain_core.output_parsers import StrOutputParser

# from app.services.retriever import get_retriever
# from app.services.llm import get_llm


# def get_rag_chain():
#     retriever = get_retriever()
#     llm = get_llm()

#     prompt = ChatPromptTemplate.from_template("""
# Answer the question using the context below.
# Be concise and clear.

# Context:
# {context}

# Question:
# {question}
# """)

#     def format_docs(docs):
#         print("\n=== RETRIEVED TEXT ===")
#         for i, doc in enumerate(docs):
#             print(f"\nChunk {i+1}:\n{doc.page_content[:800]}")
#         print("======================\n")

#         return "\n\n".join(doc.page_content for doc in docs)

#     rag_chain = (
#         {
#             "context": retriever | format_docs,
#             "question": RunnablePassthrough()
#         }
#         | prompt
#         | llm
#         | StrOutputParser()
#     )

#     return rag_chain



from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from app.services.retriever import get_retriever
from app.services.llm import get_llm


def get_rag_chain():
    retriever = get_retriever()
    llm = get_llm()

    prompt = ChatPromptTemplate.from_template("""
You are an AI assistant answering questions strictly from a provided document.

Instructions:
- Use only the information from the context.
- Do not add external knowledge.
- If the answer is not present in the context, respond exactly with:
  Not found in document.

Provide a clear and concise answer.

Context:
{context}

Question:
{question}

Answer:
""")

    def format_docs(docs):
        print("\n=== RETRIEVED TEXT ===")
        for i, doc in enumerate(docs):
            print(f"\nChunk {i+1}:\n{doc.page_content[:800]}")
        print("======================\n")

        return "\n\n---\n\n".join(doc.page_content for doc in docs)

    rag_chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain