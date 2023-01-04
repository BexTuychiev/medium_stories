import jupyter_to_medium as jtm
import os

jtm.publish('2023/1_january/1_libraries_to_watch/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="6 New Booming Data Science Libraries You Must Learn To Beat The Competition in 2023",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
