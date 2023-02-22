import jupyter_to_medium as jtm
import os

jtm.publish('2023/2_february/6_article_for_cassie/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="Inside the Black-box of Machine Learning: Linear Regression",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
