import os 
from dotenv import load_dotenv
from typing import cast

load_dotenv()

TELEGRAM_API_ID = os.getenv("TELEGRAM_API_ID")
TELEGRAM_API_HASH = cast(str, os.getenv("TELEGRAM_API_HASH"))
if not TELEGRAM_API_ID or not TELEGRAM_API_HASH:
    raise ValueError("Missing TELEGRAM_API_ID or TELEGRAM_API_HASH in .env file")

TELEGRAM_API_ID = int(TELEGRAM_API_ID)

RAW_DATA_DIR = 'data/raw/telegram_data'