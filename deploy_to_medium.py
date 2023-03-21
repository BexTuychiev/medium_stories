import jupyter_to_medium as jtm
import os

jtm.publish('2023/3_march/5_data_science_habits/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="How to Build Indestructible Data Science Learning Habits Only 5 Minutes a Day",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='matplotlib'
            )
