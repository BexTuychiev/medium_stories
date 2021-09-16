import jupyter_to_medium as jtm
import os

jtm.publish('2021/september/6_faster_pandas/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="Let's Spill the Darkest Secrets of Pandas For Working With Massive Datasets (~10M rows)",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
