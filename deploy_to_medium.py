import jupyter_to_medium as jtm
import os

jtm.publish('2021/august/4_manim_basics/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title='Love 3Blue1Brown Animations? Learn How to Create One in Python Using Manim',
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
