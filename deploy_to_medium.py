import jupyter_to_medium as jtm
import os

jtm.publish('2021/july/1_github_copilot/copilot.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title='OpenAI Launches GitHub Copilot: AI Focused On Code Generation. Should We Be Worried Now?',
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
