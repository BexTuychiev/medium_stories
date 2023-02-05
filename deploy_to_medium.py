import jupyter_to_medium as jtm
import os

jtm.publish('2023/2_february/3_outlier_detection_103/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="How to Perform Multivariate Outlier Detection in Python PyOD For Machine Learning",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
