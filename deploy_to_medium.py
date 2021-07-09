import jupyter_to_medium as jtm
import os

jtm.publish('2021/july/3_time_series_manipulation/time_series.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title='Every Function You Can (Should) Use in Pandas to Manipulate Time Series',
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
