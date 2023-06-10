import jupyter_to_medium as jtm
import os

jtm.publish('2023/6_june/2_xgb_parameters/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="10 Confusing XGBoost Hyperparameters and How to Tune Them Like a Pro in 2023",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='matplotlib'
            )
