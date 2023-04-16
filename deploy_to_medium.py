import jupyter_to_medium as jtm
import os

jtm.publish('2023/4_april/3_srs_for_data_science/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="A Proven Method To Remember Everything You Learn in Data Science (No Joke)",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='matplotlib'
            )
