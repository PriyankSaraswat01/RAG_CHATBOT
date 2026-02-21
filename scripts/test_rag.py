from app.services.rag_chain import get_rag_chain

def test():
    qa_chain = get_rag_chain()

    while True:
        query = input("Ask a question: ")
        if query.lower() == "exit":
            break

        response = qa_chain.invoke(query)
        print("\nAnswer:", response)

if __name__ == "__main__":
    test()