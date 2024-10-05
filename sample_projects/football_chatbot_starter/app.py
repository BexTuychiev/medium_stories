import streamlit as st
from langchain.chains import GraphCypherQAChain
from langchain_community.graphs import Neo4jGraph
from langchain_openai import ChatOpenAI

# Load secrets
neo4j_uri = st.secrets["NEO4J_URI"]
neo4j_user = st.secrets["NEO4J_USER"]
neo4j_password = st.secrets["NEO4J_PASSWORD"]

st.title("Football Memoirs - an AI for Hardcore Football Fans")

# Sidebar for API key input
with st.sidebar:
    openai_api_key = st.text_input("Enter your OpenAI API Key", type="password")
    st.warning("Please enter your OpenAI API key to use the chatbot.")


# Initialize connections and models
@st.cache_resource(show_spinner=False)
def init_resources(api_key):
    graph = Neo4jGraph(
        url=neo4j_uri,
        username=neo4j_user,
        password=neo4j_password,
        enhanced_schema=True,
    )
    graph.refresh_schema()

    chain = GraphCypherQAChain.from_llm(
        ChatOpenAI(api_key=api_key, model="gpt-4", temperature=0),
        graph=graph,
        verbose=True,
        show_intermediate_steps=True,
        allow_dangerous_requests=True,
    )
    return graph, chain


# Initialize resources only if API key is provided
if openai_api_key:
    with st.spinner("Initializing resources..."):
        graph, chain = init_resources(openai_api_key)
        st.success("Resources initialized successfully!", icon="🚀")


@st.cache_data(ttl=3600, show_spinner=False)  # Cache for 1 hour
def query_graph(query):
    try:
        result = chain.invoke({"query": query})["result"]
        return result
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return "I'm sorry, I encountered an error while processing your request."


# Initialize message history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! Ask me anything about International Football from 1872 to (the almost) present day!",
        }
    ]

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Your question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    if openai_api_key:
        with st.spinner("Thinking..."):
            response = query_graph(prompt)

        with st.chat_message("assistant"):
            st.markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response})
    else:
        st.error("Please enter your OpenAI API key in the sidebar to use the chatbot.")
