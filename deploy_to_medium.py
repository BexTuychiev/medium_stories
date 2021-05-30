import jupyter_to_medium as jtm
import os

jtm.publish('2021/may/9_confusion_matrix/confusion_matrix.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title='How to Tune Models like a Puppet-master Based on Confusion Matrix',
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
