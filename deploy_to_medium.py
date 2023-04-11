import jupyter_to_medium as jtm
import os

jtm.publish('2023/4_april/2_underdog_libraries/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="6 Underdog Data Science Libraries That Deserve Much More Attention",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='matplotlib'
            )
