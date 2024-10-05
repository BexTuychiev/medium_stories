# Football Memoirs - AI for Hardcore Football Fans

This Streamlit app uses a Neo4j graph database and OpenAI's GPT model to answer questions about international football history from 1872 to the present day.

## Setup

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your `.streamlit/secrets.toml` file with the following keys:
   - NEO4J_URI
   - NEO4J_USER
   - NEO4J_PASSWORD
4. Run the app: `streamlit run app.py`

## Deployment

To deploy this app on Streamlit Cloud:

1. Push your code to a GitHub repository
2. Connect your GitHub account to Streamlit Cloud
3. Create a new app in Streamlit Cloud and select your repository
4. Add your secrets in the Streamlit Cloud dashboard under the "Secrets" section
5. Deploy your app

Note: Make sure not to commit your `.streamlit/secrets.toml` file to version control.
