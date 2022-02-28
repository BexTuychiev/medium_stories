import jupyter_to_medium as jtm
import os

jtm.publish('2022/2_february/2_dvc_for_data_scientists/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="Open-source ML Project: Improve Pet Adoption With Machine Learning And DagsHub, #1",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
