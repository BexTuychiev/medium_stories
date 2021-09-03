import jupyter_to_medium as jtm
import os

jtm.publish('2021/september/2_lgbm_hp_tuning/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="Kaggler's Guide to LightGBM Hyperparameter Tuning with Optuna in 2021",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
