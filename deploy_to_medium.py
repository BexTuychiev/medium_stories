import jupyter_to_medium as jtm
import os

jtm.publish('2021/may/5_operator_overloading/operator_overloading.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title='Operator Overloading in Python OOP, Fun Tutorial',
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
