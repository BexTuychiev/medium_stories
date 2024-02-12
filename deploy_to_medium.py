import jupyter_to_medium as jtm
import os
import toml

with open('config.toml', 'r') as file:
    data = toml.load(file)

jtm.publish('2024/2_february/1_langsmith/notebook.ipynb',
            integration_token=data['codes']['TOKEN'],
            pub_name=None,
            title="An Introduction to Debugging And Testing LLMs in LangSmith",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='matplotlib'
            )
