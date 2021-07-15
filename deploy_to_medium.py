import jupyter_to_medium as jtm
import os

jtm.publish('2021/july/5_walk_noise_ts/random_walk_noise.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title='How to Detect Random Walk and White Noise in Time Series Forecasting',
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
