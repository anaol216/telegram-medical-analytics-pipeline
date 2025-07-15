from telethon import TelegramClient
from scraper.config import TELEGRAM_API_ID, TELEGRAM_API_HASH, RAW_DATA_DIR
from scraper.utils import setup_logger, save_json

import asyncio
logger = setup_logger()

channels = [
    "https://t.me/lobelia4cosmetics",
    "https://t.me/tikvahpharma"
]
async def scrape_channel(channel_url, limit = 100):
    async with TelegramClient('anon', TELEGRAM_API_ID, TELEGRAM_API_HASH) as client:
        logger.info(f"Scraping channel: {channel_url}")

    messages_data = []
    try: 
        async for message in client.iter_message(channel_url, limit=limit):
            message_dict = message.to_dict()
            messages_data.append(message_dict)
        channel_name= channel_url.split("/")[-1]
        filepath = save_json(messages_data, channel_name)
        logger
    except Exception as e:
        logger.error(f"Error scraping channel{channel_url}: {str(e)}")
    await client.disconnect()

def run_scraper():
    loop = asyncio.get_event_loop()
    tasks = [scrape_channel(channel) for channel in channels]
    loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()
run_scraper()
logger.info("Scraping completed.")