import jupyter_to_medium as jtm
import os

jtm.publish('2023/3_march/7_pandas_to_polars/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="7 Easy Steps To Switch From Pandas to Lightning Fast Polars And Never Return",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='matplotlib'
            )
