import jupyter_to_medium as jtm
import os

jtm.publish('2021/december/1_libraries_to_watch_in_2022/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="8 Dangerous Data Science Libraries You Must Watch Out in 2022",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
