import os
import jupyter_to_medium as jtm

from dotenv import load_dotenv

load_dotenv()

jtm.publish(
    "",
    integration_token=os.getenv("MEDIUM_INTEGRATION_TOKEN"),
    pub_name=None,
    title="",
    tags=None,
    publish_status="draft",
    notify_followers=False,
    license="all-rights-reserved",
    canonical_url=None,
    chrome_path=None,
    save_markdown=False,
    table_conversion="matplotlib",
)
