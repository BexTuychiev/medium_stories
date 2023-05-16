import jupyter_to_medium as jtm
import os

jtm.publish('2023/5_may/2_github_concepts/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="GitHub For The Modern Data Scientist: 7 Concepts You Can't .gitignore",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='matplotlib'
            )
