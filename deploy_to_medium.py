import jupyter_to_medium as jtm
import os

jtm.publish('2023/6_june/7_path/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="The PATH Variable For the Confused Data Scientist: How to Manage It?",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='matplotlib'
            )
