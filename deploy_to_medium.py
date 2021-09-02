import jupyter_to_medium as jtm
import os

jtm.publish('2021/september/1_lightgbm_intro/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title='How to Beat the Heck Out of XGBoost with LightGBM: Comprehensive Tutorial',
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
