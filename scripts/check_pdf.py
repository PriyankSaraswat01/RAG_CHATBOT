from app.services.loader import load_documents

docs = load_documents()

print("Total pages:", len(docs))
print("\n--- FIRST PAGE TEXT ---\n")
print(docs[0].page_content[:2000])