# import streamlit as st
# from app.services.rag_chain import get_rag_chain

# st.set_page_config(page_title="RAG Chatbot", page_icon="🤖")

# st.title("📚 RAG Chatbot")
# st.caption("Ask questions from your uploaded PDF")

# @st.cache_resource
# def load_chain():
#     return get_rag_chain()

# qa_chain = load_chain()

# # Chat memory
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display chat history
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# # Input box
# if prompt := st.chat_input("Ask a question..."):

#     # Show user message
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     # Generate response
#     with st.chat_message("assistant"):
#         with st.spinner("Thinking..."):
#             raw_response = qa_chain.invoke(prompt)

#             # ---- SMART CLEANING LOGIC ----

#             response = raw_response.strip()

#             # Remove unwanted prefixes
#             unwanted_prefixes = ["Human:", "Assistant:", "Answer:", "Context:", "Question:"]
#             for prefix in unwanted_prefixes:
#                 if response.startswith(prefix):
#                     response = response.replace(prefix, "").strip()

#             # If model echoes full prompt, extract after last "Answer:"
#             if "Answer:" in raw_response:
#                 response = raw_response.split("Answer:")[-1].strip()

#             # Final cleanup
#             response = response.strip()

#             st.markdown(response)

#     # Save assistant message
#     st.session_state.messages.append(
#         {"role": "assistant", "content": response}
#     )




import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(page_title="RAG Chatbot", page_icon="🤖")

st.title("📚 RAG Chatbot")
st.caption("Frontend → FastAPI Backend → RAG")

# Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input
if prompt := st.chat_input("Ask a question..."):

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            response = requests.post(
                API_URL,
                json={"question": prompt}
            )

            if response.status_code == 200:
                answer = response.json()["answer"]
            else:
                answer = "Error connecting to backend."

            st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )