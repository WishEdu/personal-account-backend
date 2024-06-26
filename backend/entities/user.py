from datetime import datetime
from typing import List, Optional
from dataclasses import dataclass, field, fields

from backend.configs import CLOUD_HOST


@dataclass
class Group:
    id: int
    name: str


@dataclass
class Role:
    id: int
    name: str


@dataclass
class User:
    id: int
    login: str
    email: str
    first_name: str
    last_name: str
    created_at: datetime

    description: str = ''
    background_color: str = '#005CC9'
    birthday: Optional[str] = ''
    patronymic: Optional[str] = ''
    avatar: Optional[str] = None

    groups: List[Group] = field(default_factory=list)
    roles: List[Role] = field(default_factory=list)
    permissions: List[str] = field(default_factory=list)

    def __post_init__(self):
        if self.avatar:
            self.avatar = f'{CLOUD_HOST}/assets/user/{self.id}/avatar/{self.avatar}'

        for f in fields(self):
            if self.__getattribute__(f.name) is None:
                self.__setattr__(f.name, f.default)
