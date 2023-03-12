import jupyter_to_medium as jtm
import os

jtm.publish('2023/3_march/2_impostor_syndrome/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="How to Crush the Impostor Syndrome as an (Aspiring) Data Scientist Forever",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='matplotlib'
            )
