from datetime import datetime
from typing import List, Optional
from dataclasses import dataclass, field


@dataclass
class Group:
    id: int
    name: str


@dataclass
class Role:
    id: int
    name: str


@dataclass
class UserInfo:
    id: int
    login: str
    email: str
    first_name: str
    last_name: str
    created_at: datetime

    background_color: Optional[str] = '1B365D'
    patronymic: Optional[str] = None
    birthday: Optional[str] = None

    groups: List[Group] = field(default_factory=list)
    roles: List[Role] = field(default_factory=list)
    permissions: List[str] = field(default_factory=list)


