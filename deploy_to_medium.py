import jupyter_to_medium as jtm
import os
import toml

with open("config.toml", "r") as file:
    data = toml.load(file)

jtm.publish(
    "2024/8_august/2_rag_langchain/notebook.ipynb",
    integration_token=data["codes"]["TOKEN"],
    pub_name=None,
    title="Building a RAG system with LangChain",
    tags=None,
    publish_status="draft",
    notify_followers=False,
    license="all-rights-reserved",
    canonical_url=None,
    chrome_path=None,
    save_markdown=False,
    table_conversion="matplotlib",
)
