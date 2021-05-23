import os
from telethon.tl.types import ChatBannedRights



class Config(object):
    LOGGER = True


AUTONAME = os.environ.get("AUTONAME", None)
CHANGE_TIME = int(os.environ.get("CHANGE_TIME", 60))


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
