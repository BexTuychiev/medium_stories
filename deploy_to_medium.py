import jupyter_to_medium as jtm
import os

jtm.publish('2021/july/8_xgboost_faqs/faqs.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title='20 Burning XGBoost FAQs Answered to Use the Library Like a Pro',
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
