import jupyter_to_medium as jtm

jtm.publish('merge_data_article/main.ipynb',
            integration_token="222f6677e2c8d29a810fc29db5f70b51086db498986340647485c9ba6c3f345dc",
            pub_name=None,
            title=None,
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
