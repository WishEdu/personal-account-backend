from re import fullmatch
from dataclasses import dataclass, fields, asdict
from typing import get_args


regex_config = {
    'login': r'[a-z0-9_]{4,32}',
    'password': r'((?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,20})',
    'email': r'^(.+)@(.+)\.(.+)$',
    'first_name': r'[А-ЯЁ]{1}[а-яё ]{1,255}',
    'last_name': r'[А-ЯЁ]{1}[а-яё ]{1,255}',
    'patronymic': r'[А-ЯЁ]{1}[а-яё ]{1,255}',
    'birthday': r'(19|20)\d\d-((0[1-9]|1[012])-(0[1-9]|[12]\d)|(0[13-9]|1[012])-30|(0[13578]|1[02])-31)',
    'background_color': r'^#(?:[0-9a-fA-F]{3}){1,2}$'
}

regex_messages = {
    'login': 'Логин может содержать от 4 до 32 символов, среди них: строчные латинские буквы, цифры и нижнее подчёркивание.',
    'password': 'Пароль должен быть не короче 8 символов, среди них: Строчные и прописные латинские буквы, цифры.',
    'email': 'Неверный формат электронной почты.',
    'first_name': 'Некорректный формат имени.',
    'last_name': 'Некорректный формат фамилии.',
    'patronymic': 'Некорректный формат отчества.',
    'birthday':'День рождения должен быть в формате год-месяц-день',
    'background_color':r'Цвет фона должен быть в формате hex с # в начале'
}


@dataclass
class BaseFormClass:

    @property
    def get_validation(self):
        for f in fields(self):
            value = asdict(self)[f.name]
            _type = get_args(f.type) or (f.type,)

            if isinstance(value, str) and not fullmatch(regex_config.get(f.name, '.'), value) and type(None) not in _type:
                return {'errorMessage': regex_messages.get(f.name, f'Ошибка валидации поля {f.name}')}
            elif _type[0] != type(value) and value != f.default:
                return {'errorMessage': f'Поле {f.name} со значением: {value} имеет некорректный тип данных'}

        return True

