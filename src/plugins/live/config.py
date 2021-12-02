from typing import List
from pydantic import BaseSettings


class Config(BaseSettings):

    # plugin custom config
    room_ids: List[str] = []
    subscribers: List[str] = []
    live_check_interval: int = 60

    class Config:
        extra = "ignore"
