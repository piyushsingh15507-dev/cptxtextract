import os
from os import getenv


API_ID = int(getenv("API_ID", 36317039))
API_HASH = getenv("API_HASH", "63a3043f21587a8ef3d341d3901d86ab")
BOT_TOKEN = getenv("BOT_TOKEN", "5887516185:AAHbYz8_89S0N2h2vzaQxQHxf1XjZ_o-10o")
OWNER_ID = int(getenv("OWNER_ID", "6821417645"))
SUDO_USERS = 6821417645
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://piyushsingh15507_db_user:tC7SZxBcBiXnVxU3@cpext.m6cymxf.mongodb.net/?retryWrites=true&w=majority&appName=CPEXT")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1003553512208"))
