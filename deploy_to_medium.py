import jupyter_to_medium as jtm
import os

jtm.publish('2022/2_february/3_image_processing/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="Massive Post on Image Processing And Preparation For Deep Learning in Python",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
