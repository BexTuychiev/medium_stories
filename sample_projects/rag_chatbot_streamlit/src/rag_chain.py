import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

# Load environment variables
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

RAG_PROMPT_TEMPLATE = """
You are a helpful coding assistant that can answer questions about the provided context. The context is usually a PDF document or an image (screenshot) of a code file. Augment your answers with code snippets from the context if necessary.

If you don't know the answer, say you don't know.

Context: {context}
Question: {question}
"""
PROMPT = PromptTemplate.from_template(RAG_PROMPT_TEMPLATE)


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def create_rag_chain(chunks):
    embeddings = OpenAIEmbeddings(api_key=api_key)
    doc_search = Chroma.from_documents(chunks, embeddings)
    retriever = doc_search.as_retriever(
        search_type="similarity", search_kwargs={"k": 5}
    )
    llm = ChatOpenAI(model_name="gpt-4o", temperature=0)

    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | PROMPT
        | llm
        | StrOutputParser()
    )

    return rag_chain


if __name__ == "__main__":
    from document_processor import process_document

    # Assuming you have a source file path
    source_file = "/home/bexgboost/articles/sample_projects/rag_chatbot_streamlit/src/unscanned.pdf"  # Replace with actual path
    chunks = process_document(source_file)
    rag_chain = create_rag_chain(chunks)
    print(
        rag_chain.invoke("How to create a Neo4j reading chain? Write me the full code")
    )
