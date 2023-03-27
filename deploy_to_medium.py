import jupyter_to_medium as jtm
import os

jtm.publish('2023/3_march/6_polars_vs_pandas/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="Measuring The Speed of New Pandas 2.0 Against Polars and Datatable - Still Not Good Enough",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='matplotlib'
            )
