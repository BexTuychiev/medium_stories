import jupyter_to_medium as jtm
import os

jtm.publish('2023/4_april/1_pathlib/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="Goodbye os.path: 15 Pathlib Tricks to Quickly Master The File System in Python",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='matplotlib'
            )
