import os

API_ID = API_ID = 28748671

API_HASH = os.environ.get("API_HASH", "f53ec7c41ce34e6d585674ed9ce6167c")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7791056995:AAGTt6xsnHrcST6V496hzHlht1RpO-be1lc")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 1169394017))

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1169394017").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


