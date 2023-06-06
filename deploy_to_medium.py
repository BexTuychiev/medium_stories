import jupyter_to_medium as jtm
import os

jtm.publish('2023/6_june/1_docker_concepts/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="Docker For the Modern Data Scientists: 6 Concepts You Can't Ignore in 2023",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='matplotlib'
            )
