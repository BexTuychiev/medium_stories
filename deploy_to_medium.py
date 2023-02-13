import jupyter_to_medium as jtm
import os

jtm.publish('2023/2_february/4_signs_of_pro/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="5 Signs You've Become an Advanced Pythonista Without Even Realizing It",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
