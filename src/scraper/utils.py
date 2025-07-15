import os
import json
import logging
from datetime import datetime

def setup_logger():
    logging.basicConfig(
        level= logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler()]
    )
    return logging.getLogger("telegram_scraper")
def save_json(data, channel_name):

    today = datetime.now().strftime("%Y-%m-%d")
    directory= os.path.join('data', 'raw', 'telegram_data', today)
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, f"{channel_name}.json")
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return file_path