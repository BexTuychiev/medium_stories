import jupyter_to_medium as jtm
import os

jtm.publish('2022/4_april/1_easiest_model_deployment_pet_part_3/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="The Easiest Way to Deploy Your ML/DL Models in 2022: Streamlit + BentoML + DagsHub",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
