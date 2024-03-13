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
    login: Optional[str] = None
    email: Optional[str] = None

    @property
    def auth(self):
        return 'email' if self.email is not None else 'login', self.email or self.login

