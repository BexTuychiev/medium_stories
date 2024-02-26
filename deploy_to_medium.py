import jupyter_to_medium as jtm
import os
import toml

with open('config.toml', 'r') as file:
    data = toml.load(file)

jtm.publish('2024/2_february/3_ag_data_clean/notebook.ipynb',
            integration_token=data['codes']['TOKEN'],
            pub_name=None,
            title="How to Explore and Clean Sensitive Data You Can't Even See With Antigranular",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='matplotlib'
            )
