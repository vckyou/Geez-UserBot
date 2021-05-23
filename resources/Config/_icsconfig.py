import os
from telethon.tl.types import ChatBannedRights


AUTONAME = os.environ.get("AUTONAME", None)
CHANGE_TIME = int(os.environ.get("CHANGE_TIME", 60))
