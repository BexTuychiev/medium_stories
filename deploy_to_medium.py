import jupyter_to_medium as jtm
import os

jtm.publish('2023/5_may/5_sklearn_pipelines/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="Sklearn Pipelines for the Modern ML Engineer: 9 Techniques You Can't Ignore",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='matplotlib'
            )
