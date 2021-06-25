import jupyter_to_medium as jtm
import os

jtm.publish('2021/june/7_tasks_during_model_training/tasks_during_model_training.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title='5 Short But Super Productive Things To Do During Model Training',
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
