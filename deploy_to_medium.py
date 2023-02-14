import jupyter_to_medium as jtm
import os

jtm.publish('2023/2_february/5_dealing_with_outliers/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="What to Do With Outliers Once You Find Them? (Hint: You Can't Drop Them)",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
