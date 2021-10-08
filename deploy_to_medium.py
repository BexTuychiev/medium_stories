import jupyter_to_medium as jtm
import os

jtm.publish('2021/october/2_sklearn_features_2/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="10 Underrated Sklearn Features You Can Use For Your Advantage Right Now",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
