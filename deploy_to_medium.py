import jupyter_to_medium as jtm
import os

jtm.publish('2023/5_may/1_pandas_pro/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="5 Signs You've Become an Advanced Pandas User Without Even Realizing It",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='matplotlib'
            )
