import jupyter_to_medium as jtm
import os

jtm.publish('2023/6_june/6_future_pythons/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="How to Access Future Python Versions Like 3.12 Before the Masses",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='matplotlib'
            )
