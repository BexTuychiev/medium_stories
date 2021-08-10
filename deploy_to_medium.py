import jupyter_to_medium as jtm
import os

jtm.publish('2021/august/3_masterpiece_matplotlib/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title='Yes, These Unbelievable Masterpieces Are Created With Matplotlib',
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
