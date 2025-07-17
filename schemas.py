from pydantic import BaseModel
from typing import List, Optional

class TopProduct(BaseModel):
    detected_object_class: str
    count: int

class ChannelActivity(BaseModel):
    message_date: str
    total_messages: int

class MessageSearchResult(BaseModel):
    message_id: int
    message_date: str
    channel_name: str
    media_exists: bool
