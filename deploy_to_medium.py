import jupyter_to_medium as jtm
import os

jtm.publish('2021/october/3_pandas_mistakes/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="6 Pandas Mistakes That Silently Tell You Are a Rookie",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
