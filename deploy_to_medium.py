import jupyter_to_medium as jtm
import os

jtm.publish('2021/',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title='How to Manage Attribute and Data Access in Python Classes',
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
