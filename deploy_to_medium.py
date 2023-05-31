import jupyter_to_medium as jtm
import os

jtm.publish('2023/5_may/7_sklearn_pro/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="7 Signs You've Become an Advanced Sklearn User Without Even Realizing It",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='matplotlib'
            )
