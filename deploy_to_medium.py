import jupyter_to_medium as jtm
import os

jtm.publish('2021/march/3_plotly_pandas_backend/plotly_backed.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title=None,
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
