-- models/staging/stg_telegram_messages.sql

with source as (

    select
        message_id,
        cast(date as timestamp) as message_date,
        channel_name,
        message_text,
        media_exists
    from {{ source('public', 'raw_telegram_messages') }}

)

select * from source
