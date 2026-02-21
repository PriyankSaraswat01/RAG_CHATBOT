from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from app.services.retriever import get_retriever
from app.services.llm import get_llm


def get_rag_chain():
    retriever = get_retriever()
    llm = get_llm()

    prompt = ChatPromptTemplate.from_template("""
Answer the question using only the context below.
Give a clear explanation in 3–4 sentences.
Write in a natural paragraph format.
Do NOT repeat the question.
Do NOT mention the word 'Context' or 'Question'.

Context:
{context}

Question:
{question}

Answer:
""")

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

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