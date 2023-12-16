import jupyter_to_medium as jtm
import os

jtm.publish('2023/12_december/1_gradient_boosting/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="A Guide to the Gradient Boosting Algorithm",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='matplotlib'
            )
