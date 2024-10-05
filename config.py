from os import getenv
from dotenv import load_dotenv

load_dotenv()


class Config:
    TELEGRAM_TOKEN = getenv("TELEGRAM_TOKEN")

    OPENAI_KEY = getenv("OPENAI_KEY")
    OPENAI_URL = getenv("OPENAI_URL")
    OPENAI_MODEL = getenv("OPENAI_MODEL")
