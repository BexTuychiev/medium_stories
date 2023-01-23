import jupyter_to_medium as jtm
import os

jtm.publish('2023/1_january/4_julia_vs_python/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="5 Excellent Julia Features That Python Developers Can Only Wish They Had",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
