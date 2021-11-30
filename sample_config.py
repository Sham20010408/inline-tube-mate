# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Name     : inline-tube-mate [ Telegram ]
# Repo     : https://github.com/m4mallu/inine-tube-mate
# Author   : Renjith Mangal [ https://t.me/space4renjith ]
# Credits  : https://github.com/SpEcHiDe/AnyDLBot


import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):
    # Get a bot token from botfather
    TG_BOT_TOKEN = 2111988625:AAFzbM-eAT_5oGMS-bDsz18dJlSNa0aHKbo

    # Get from my.telegram.org
    APP_ID = 1424314

    # Get from my.telegram.org
    API_HASH = d1c1c9262bbae8f5eeb80ba47c9f3dff

    # Authorized user ids to use this bot
    AUTH_USERS = 1079261681

    # Super users to broadcast messages & fetch subscribers count
    SUDO_USERS = 1079261681

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "")

    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    # Telegram maximum file upload size
    TG_MAX_FILE_SIZE = 2097152000

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
