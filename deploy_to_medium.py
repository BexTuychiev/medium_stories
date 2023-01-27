import jupyter_to_medium as jtm
import os

jtm.publish('2023/1_january/5_outlier_detection_101/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="How to Perform Outlier Detection In Python In Easy Steps For Machine Learning, #1",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
