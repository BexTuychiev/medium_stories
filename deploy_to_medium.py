import jupyter_to_medium as jtm
import os

jtm.publish('2021/august/1_pandas_funcs/pandas_funcs.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title='25 Pandas Functions You Didn\'t Know Existed | P(Guarantee) = 0.8',
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
