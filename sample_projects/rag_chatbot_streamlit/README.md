# RAG Chatbot

This is a Retrieval-Augmented Generation (RAG) chatbot built with Streamlit and LangChain.

## Setup

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`
4. Install the requirements: `pip install -r requirements.txt`
5. Run the app: `streamlit run app.py`

## Usage

1. Enter your OpenAI API key in the sidebar
2. Select the source type and enter the source URL or file path
3. Click "Load Source" to process the document
4. Enter your question and click "Ask" to get an answer

## Deployment

This app can be deployed on Streamlit Cloud:

1. Push your code to a GitHub repository
2. Log in to [Streamlit Cloud](https://streamlit.io/cloud)
3. Create a new app and select your GitHub repository
4. Configure the app settings (Python version, requirements file, etc.)
5. Deploy the app

Remember to set the `OPENAI_API_KEY` as a secret in your Streamlit Cloud app settings for production use.
