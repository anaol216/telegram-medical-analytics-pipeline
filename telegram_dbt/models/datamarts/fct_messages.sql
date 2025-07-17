with messages as (
    select * from {{ ref('stg_telegram_messages') }}
)

select
    message_id,
    channel_name,
    message_date,
    length(message_text) as message_length,
    media_exists
from messages
