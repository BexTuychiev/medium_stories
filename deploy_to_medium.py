import jupyter_to_medium as jtm
import os

jtm.publish('2022/1_january/3_aws_s3/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="How to Upload And Download Files From AWS S3 Using Python (2022)",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
