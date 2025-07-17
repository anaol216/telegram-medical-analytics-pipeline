from pathlib import Path
from telethon import TelegramClient
from scraper.config import TELEGRAM_API_ID, TELEGRAM_API_HASH, RAW_DATA_DIR
from scraper.utils import setup_logger, save_json

import asyncio

logger = setup_logger()

channels = [
    "https://t.me/lobelia4cosmetics",
    "https://t.me/tikvahpharma"
]

async def scrape_channel(channel_url, limit=100):
    channel_name = channel_url.split("/")[-1]
    session_name = f'session_{channel_name}'

    async with TelegramClient(session_name, int(TELEGRAM_API_ID), TELEGRAM_API_HASH) as client:
        logger.info(f"Scraping channel: {channel_url}")

        messages_data = []

        try:
            async for message in client.iter_messages(channel_url, limit=limit):
                message_dict = {
                    "message_id": message.id,
                    "date": str(message.date),
                    "channel_name": channel_name,
                    "message_text": message.message if message.message else "",
                    "media_exists": message.media is not None
                }

                if message.photo:
                    media_file_path = Path(RAW_DATA_DIR) / f"{channel_name}_{message.id}.jpg"
                    await message.download_media(file=media_file_path)
                    message_dict["media_file_path"] = str(media_file_path)
                else:
                    message_dict["media_file_path"] = None
                    message_dict["media_file_path"] = None

                messages_data.append(message_dict)

            filepath = save_json(messages_data, channel_name)
            logger.info(f"Saved {len(messages_data)} messages from {channel_name} at {filepath}")

        except Exception as e:
            logger.error(f"Error scraping channel {channel_url}: {str(e)}")


def run_scraper():
    loop = asyncio.get_event_loop()
    tasks = [scrape_channel(channel) for channel in channels]
    loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()
    logger.info("Scraping completed.")