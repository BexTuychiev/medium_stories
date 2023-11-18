import jupyter_to_medium as jtm
import os

jtm.publish('2023/11_november/1_anomaly_detection/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="Anomaly detection",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='matplotlib'
            )
