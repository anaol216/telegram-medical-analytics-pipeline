with base as (
    select distinct message_date::date as date_day
    from {{ ref('stg_telegram_messages') }}
)

select
    date_day,
    extract(year from date_day) as year,
    extract(month from date_day) as month,
    extract(day from date_day) as day
from base
