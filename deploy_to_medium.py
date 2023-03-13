import jupyter_to_medium as jtm
import os

jtm.publish('2023/3_march/3_format_string_codes/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="Have Mercy on Yourself And Learn These 9 Everyday Python f-string Codes",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='matplotlib'
            )
