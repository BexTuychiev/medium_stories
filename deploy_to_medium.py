import jupyter_to_medium as jtm
import os

jtm.publish('november_2020/string_matching_w_fuzzy_wuzzy/fuzzy_wuzzy.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title=None,
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
