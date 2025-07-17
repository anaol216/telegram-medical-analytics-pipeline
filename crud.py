from database import get_db_connection

def get_top_products(limit: int):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
        SELECT detected_object_class, COUNT(*) as count
        FROM fct_image_detections
        GROUP BY detected_object_class
        ORDER BY count DESC
        LIMIT %s;
    """
    cursor.execute(query, (limit,))
    result = [
        {"detected_object_class": row[0], "count": row[1]}
        for row in cursor.fetchall()
    ]

    cursor.close()
    conn.close()
    return result


def get_channel_activity(channel_name: str):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
        SELECT message_date::date, COUNT(*) as total_messages
        FROM fct_messages
        WHERE channel_name = %s
        GROUP BY message_date::date
        ORDER BY message_date::date;
    """
    cursor.execute(query, (channel_name,))
    result = [
        {"message_date": str(row[0]), "total_messages": row[1]}
        for row in cursor.fetchall()
    ]

    cursor.close()
    conn.close()
    return result


def search_messages(query: str):
    conn = get_db_connection()
    cursor = conn.cursor()

    query_sql = """
        SELECT message_id, date as message_date, channel_name, message_text, media_exists
        FROM raw_telegram_messages
        WHERE message_text ILIKE %s
        ORDER BY date DESC
        LIMIT 100;
    """
    cursor.execute(query_sql, (f"%{query}%",))
    result = [
        {
            "message_id": row[0],
            "message_date": str(row[1]),
            "channel_name": row[2],
            "media_exists": row[4]
        }
        for row in cursor.fetchall()
    ]

    cursor.close()
    conn.close()
    return result
