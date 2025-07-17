
-- Use the `ref` function to select from other models

select *
from {{ ref('telegram_messages') }}
where message_id = 1
