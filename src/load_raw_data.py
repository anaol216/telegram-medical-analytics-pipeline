import psycopg2
import json
import os

# Adjust the path to your actual raw data folder
RAW_DATA_DIR = './data/raw'

# Connect to PostgreSQL running inside Docker, but exposed to localhost
conn = psycopg2.connect(
    host="localhost",     # <-- Important: localhost when running outside Docker
    port="5432",
    database="telegramdb",
    user="postgres",
    password="postgres"
)

cursor = conn.cursor()

# Loop through your JSON files
for filename in os.listdir(RAW_DATA_DIR):
    if filename.endswith('.json'):
        filepath = os.path.join(RAW_DATA_DIR, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            messages = json.load(f)
            for message in messages:
                cursor.execute("""
                    INSERT INTO raw_telegram_messages (message_id, date, channel_name, message_text, media_exists)
                    VALUES (%s, %s, %s, %s, %s)
                    ON CONFLICT (message_id) DO NOTHING;
                """, (
                    message.get('message_id'),
                    message.get('date'),
                    message.get('channel_name'),
                    message.get('message_text'),
                    message.get('media_exists')
                ))

conn.commit()
cursor.close()
conn.close()
print("✅ Data loaded successfully.")
