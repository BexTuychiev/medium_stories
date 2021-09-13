import jupyter_to_medium as jtm
import os

jtm.publish('2021/september/5_sklearn_transformers/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="How to Write Powerful Code Others Envy With Custom Sklearn Transformers",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
