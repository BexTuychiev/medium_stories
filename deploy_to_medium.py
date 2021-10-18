import jupyter_to_medium as jtm
import os

jtm.publish('2021/october/4_numpy_functions_didnt_see/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="20 NumPy Functions You Never Knew Existed | P (Guarantee = 0.85)",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
