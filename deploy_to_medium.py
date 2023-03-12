import jupyter_to_medium as jtm
import os

jtm.publish('2023/2_february/7_fractal_art/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="Create Stunning Fractal Art with Python: A Tutorial For Beginners And Hardcore Math Lovers",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='matplotlib'
            )
