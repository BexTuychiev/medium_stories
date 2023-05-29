import jupyter_to_medium as jtm
import os

jtm.publish('2023/5_may/6_args_kwargs/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="Clearing the Confusion Once And For All: args, kwargs, and asterisks in Python",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='matplotlib'
            )
