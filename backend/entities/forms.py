from dataclasses import dataclass
from typing import Optional
from backend.entities import BaseFormClass


@dataclass
class RegistrationForm(BaseFormClass):
    login: str
    password: str
    email: str
    first_name: str
    last_name: str
    patronymic: Optional[str] = ''


@dataclass
class LoginForm(BaseFormClass):

    password: str
    login: str


@dataclass
class ConfirmEmailForm(BaseFormClass):
    user_id: int
    email: str


@dataclass
class UserEditForm(BaseFormClass):
    background_color: str

    first_name: str
    last_name: str
    patronymic: Optional[str] = ''

    birthday: Optional[str] = ''
    description: Optional[str] = ''



