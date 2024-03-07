import jupyter_to_medium as jtm
import os
import toml

with open('config.toml', 'r') as file:
    data = toml.load(file)

jtm.publish('2024/3_march/3_snowflake_time_travel/notebook.ipynb',
            integration_token=data['codes']['TOKEN'],
            pub_name=None,
            title="Comprehensive Guide on Using Time Travel Feature in Snowflake",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='matplotlib'
            )
