import jupyter_to_medium as jtm
import os

jtm.publish('2021/june/3_sql_fundamentals/sql_fundamentals.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title='Master SQL Fundamentals Effortlessly as a Pandas User',
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
