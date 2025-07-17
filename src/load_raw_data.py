import psycopg2
import json
import os

RAW_DATA_DIR = './data/raw'

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="telegramdb",
    user="postgres",
    password="postgres"
)

cursor = conn.cursor()

for root, dirs, files in os.walk(RAW_DATA_DIR):
    for filename in files:
        if filename.endswith('.json'):
            filepath = os.path.join(root, filename)
            print(f"Loading data from: {filepath}")
            with open(filepath, 'r', encoding='utf-8') as f:
                messages = json.load(f)
                for message in messages:
                    try:
                        print(f"Inserting message_id: {message.get('message_id')}")
                        cursor.execute("""
                            INSERT INTO raw_telegram_messages (message_id, date, channel_name, message_text, media_exists,media_file_path)
                            VALUES (%s, %s, %s, %s, %s, %s)
                            ON CONFLICT (message_id) DO NOTHING;
                        """, (
                            message.get('message_id'),
                            message.get('date'),
                            message.get('channel_name'),
                            message.get('message_text'),
                            message.get('media_exists'),
                            message.get('media_file_path')  # Assuming media_exists is a boolean
                        ))
                    except Exception as e:
                        print(f"Error inserting message {message.get('message_id')}: {e}")

conn.commit()
cursor.close()
conn.close()
print("✅ Data loaded successfully.")
