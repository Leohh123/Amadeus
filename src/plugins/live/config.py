from typing import List
from pydantic import BaseSettings


class Config(BaseSettings):

    # plugin custom config
    room_ids: List[str] = []
    subscribers: List[str] = []

    class Config:
        extra = "ignore"
