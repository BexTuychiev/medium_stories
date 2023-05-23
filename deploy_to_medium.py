import jupyter_to_medium as jtm
import os

jtm.publish('2023/5_may/4_dvc_concepts/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="Data Version Control For the Modern Data Scientist: 7 DVC Concepts You Can't Ignore",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='matplotlib'
            )
