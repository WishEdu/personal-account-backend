from datetime import datetime
from typing import Optional
from dataclasses import dataclass


@dataclass
class User:
    id: int
    login: str
    email: str
    first_name: str
    last_name: str
    created_at: datetime

    background_color: Optional[str] = '1B365D'
    patronymic: Optional[str] = None
    birthday: Optional[str] = None


