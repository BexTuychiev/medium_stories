import jupyter_to_medium as jtm
import os

jtm.publish('2021/october/9_matplotlib_functions/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="10 Advanced Matplotlib Concepts You Must Know To Create Killer Visuals",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
