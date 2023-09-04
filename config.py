from os import getenv
from dotenv import load_dotenv

import openai
openai.api_key = ""
openai.api_base = "http://localhost:1337"

load_dotenv()


class Config:
    TELEGRAM_TOKEN = getenv("TELEGRAM_TOKEN")
    DATABASE_URL = getenv("DATABASE_URL")
    OPENAI_API = getenv("OPENAI_API")
