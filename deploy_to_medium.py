import jupyter_to_medium as jtm
import os

jtm.publish('2021/august/2_popular_kaggle_packages/kaggle_packages.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title='7 Coolest Python Packages Kagglers Are Using Without Telling You',
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
