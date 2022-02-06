import jupyter_to_medium as jtm
import os

jtm.publish('2022/2_february/1_julia_for_pythoneers/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="10-Minute Guide to Julia For Die-Hard Python Lovers",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
