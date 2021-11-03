import jupyter_to_medium as jtm
import os

jtm.publish('2021/november/1_thousands_for_ds/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="How I Earn Thousands For Learning Data Science With No Degree and Experience",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
