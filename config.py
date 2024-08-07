import os, re


BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
OWNER = int(os.environ.get("OWNER", ""))
BOT_USERNAME = os.environ.get('BOT_USERNAME', "")

FORCE_SUBS = os.environ.get("FORCE_SUBS", "TheBlackXYZ")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))

DB_URL = os.environ.get("DB_URL", "")
DB_NAME = os.environ.get("DB_NAME", "Cluster0")

STRING = os.environ.get("STRING", "")
BOT_PIC = os.environ.get("BOT_PIC", "")



# if you need to add verify system then dm me on telegram

SHORTNER_URL = os.environ.get("SHORTNER_URL", "")
SHORTNER_API = os.environ.get("SHORTNER_API", "")
TOKEN_TIMEOUT = os.environ.get("TOKEN_TIMEOUT", "")
