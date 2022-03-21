import jupyter_to_medium as jtm
import os

jtm.publish('2022/3_march/2_ml_experimentation/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="Complete Guide to Tracking Your Machine Learning Experiments With MLFlow and DagsHub",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
