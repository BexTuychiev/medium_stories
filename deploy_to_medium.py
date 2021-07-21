import jupyter_to_medium as jtm
import os

jtm.publish('2021/july/7_ts_feature_engineering/ts_feature_engineering.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title='Top 4 Time Series Feature Engineering Lessons From Kaggle',
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
