-- models/telegram_messages.sql

SELECT
    message_id,
    date,
    channel_name,
    message_text,
    media_exists
FROM {{ source('public', 'raw_telegram_messages') }}
