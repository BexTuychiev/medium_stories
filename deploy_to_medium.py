import jupyter_to_medium as jtm
import os

jtm.publish('2021/august/6_best_datasets/best_datasets.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title='Tired of Cliché Datasets? Here are 18 Unique Alternatives From All Domains',
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
