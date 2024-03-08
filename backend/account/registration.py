from dataclasses import astuple, asdict
from flask import request
from flask_cors import cross_origin
from json import dumps
from logging import error

from backend.account import account_bp

from backend.modules.queries import CREATE_USER_QUERY
from backend.modules.database import cursor, db
from backend.modules.user import get_user
from backend.modules.session_manager import create_session
from backend.modules.code_generator import get_hash

from backend.entities.forms import RegistrationForm


@account_bp.post('/registration')
@cross_origin()
def registration_handler():
    browser = request.headers.get('browser')

    if browser is None:
        return dumps({'errorMessage': 'Неверные данные запроса.'}, ensure_ascii=False), 403

    data = request.json
    try:
        user = RegistrationForm(**data)
    except TypeError:
        return dumps({'errorMessage': 'Недопустимые значения полей. Смотрите документацию.'}, ensure_ascii=False), 400

    is_valid = user.get_validation

    if is_valid is not True:
        return dumps(is_valid), 400

    cursor.execute("SELECT login, email FROM users WHERE login = %s OR email = %s", (user.login, user.email))
    exists = cursor.fetchone()

    if exists:
        error_message = 'Электронный адрес'
        if exists['login'] == user.login:
            error_message = 'Логин'
        return dumps({'errorMessage': f'{error_message} уже зарегистрирован.'}, ensure_ascii=False), 400

    user.password = get_hash(user.password)

    try:
        cursor.execute(CREATE_USER_QUERY, astuple(user))
    except Exception as E:
        db.rollback()
        error(f'Registration DB error: {E} | USER INFO: {user}', exc_info=True)
        return dumps({'errorMessage': 'Ошибка транзакции в базе данных. Сообщите разработчикам.'},
                     ensure_ascii=False), 500

    db.commit()

    user_id = cursor.fetchone()['id']
    user = get_user(id=user_id)

    return dumps({**asdict(user), 'token': create_session(user, browser, request.remote_addr)}, ensure_ascii=False, default=str), 200
