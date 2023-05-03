import jupyter_to_medium as jtm
import os

jtm.publish('2023/4_april/4_git_for_data_scientists/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="Git For the Modern Data Scientist: 9 Git Concepts You Can't Ignore",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='matplotlib'
            )
