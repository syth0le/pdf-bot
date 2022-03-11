import os

from dotenv import load_dotenv

load_dotenv(override=True)

IS_POSTING_REQUESTED = True


class BotConfig:
    API_TOKEN = os.getenv('API_TOKEN')
    ACCESS_ID = os.getenv('ACCESS_ID')
    USERNAME = os.getenv('USERNAME')
    CHAT_ID = os.getenv('CHAT_ID')
