import jupyter_to_medium as jtm
import os

jtm.publish('2021/july/4_advanced_ts_visuals/ts_visualize.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title='Advanced Time Series Analysis in Python: Seasonality and Trend Analysis (Decomposition), Autocorrelation',
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
