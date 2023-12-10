import jupyter_to_medium as jtm
import os

jtm.publish('2023/11_november/3_mysql_docker/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="MySQL + Docker",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='matplotlib'
            )
