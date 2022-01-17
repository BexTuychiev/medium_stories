import jupyter_to_medium as jtm
import os

jtm.publish('2022/1_january/2_terality/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="Good-bye Pandas! Meet Terality - Its Evil Twin With Identical Syntax",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
