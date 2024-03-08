from re import fullmatch
from dataclasses import dataclass, fields, asdict
from typing import get_args

regex_config = {
    'login': r'[a-z0-9_]{4,32}',
    'password': r'((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[\W]).{8,20})',
    'email': r'^(.+)@(.+)\.(.+)$',
    'first_name': r'[А-Я]{1}[а-я ]{1,255}',
    'last_name': r'[А-Я]{1}[а-я ]{1,255}',
    'patronymic': r'[А-Я]{1}[а-я ]{1,255}',
    'birthday': r'(19|20)\d\d-((0[1-9]|1[012])-(0[1-9]|[12]\d)|(0[13-9]|1[012])-30|(0[13578]|1[02])-31)',
}


@dataclass
class BaseFormClass:

    @property
    def get_validation(self):
        for f in fields(self):
            value = asdict(self)[f.name]
            _type = (get_args(f.type) or (f.type,))[0]

            if isinstance(value, str) and not fullmatch(regex_config[f.name], value):
                return {'errorMessage': f'Поле {f.name} со значением: {value} не прошло валидацию.'}
            elif _type != type(value) and value != f.default:
                return {'errorMessage': f'Поле {f.name} со значением: {value} имеет некорректный тип данных'}

        return True

