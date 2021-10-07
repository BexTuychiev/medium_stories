import jupyter_to_medium as jtm
import os

jtm.publish('2021/october/1_shap_explainability/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="Model Explainability with SHAP: A Guide to Those Who Are Serious About Machine Learning",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
