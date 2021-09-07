import jupyter_to_medium as jtm
import os

jtm.publish('2021/september/4_mln_row_datasets/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="How to Work with Million-row Datasets Like a Pro",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
