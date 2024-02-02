import jupyter_to_medium as jtm
import os
import toml

with open('config.toml', 'r') as file:
    data = toml.load(file)

jtm.publish('2024/1_january/4_intro_to_nannyml/notebook.ipynb',
            integration_token=data['codes']['TOKEN'],
            pub_name=None,
            title="An end-to-end ML Model Monitoring Workflow with NannyML in Python",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='matplotlib'
            )
