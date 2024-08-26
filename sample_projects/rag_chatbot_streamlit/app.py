import streamlit as st
import os
from dotenv import load_dotenv
from src.document_processor import process_document
from src.rag_chain import create_rag_chain

# Load environment variables
load_dotenv()

st.set_page_config(page_title="RAG Chatbot", page_icon="🤖")

st.title("RAG Chatbot")

# Initialize session state
if "rag_chain" not in st.session_state:
    st.session_state.rag_chain = None

# Sidebar for API key input
with st.sidebar:
    api_key = st.text_input("Enter your OpenAI API Key", type="password")
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key

# File uploader
uploaded_file = st.file_uploader("Choose a file", type=["pdf", "png", "jpg", "jpeg"])

if uploaded_file is not None:
    if st.button("Process File"):
        if api_key:
            with st.spinner("Processing file..."):
                # Save the uploaded file temporarily
                with open(uploaded_file.name, "wb") as f:
                    f.write(uploaded_file.getbuffer())

                try:
                    # Process the document
                    chunks = process_document(uploaded_file.name)

                    # Create RAG chain
                    st.session_state.rag_chain = create_rag_chain(chunks)

                    st.success("File processed successfully!")
                except ValueError as e:
                    st.error(str(e))
                finally:
                    # Remove the temporary file
                    os.remove(uploaded_file.name)
        else:
            st.error("Please provide your OpenAI API key.")

# Query input
query = st.text_input("Ask a question about the uploaded document")

if st.button("Ask"):
    if st.session_state.rag_chain and query:
        with st.spinner("Generating answer..."):
            result = st.session_state.rag_chain.invoke(query)

            st.subheader("Answer:")
            st.write(result)
    elif not st.session_state.rag_chain:
        st.error("Please upload and process a file first.")
    else:
        st.error("Please enter a question.")
