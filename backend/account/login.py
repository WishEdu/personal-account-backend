from json import dumps
from re import fullmatch
from dataclasses import asdict

from logging import error
from flask import request
from flask_cors import cross_origin

from . import account_bp
from backend.modules.user import action_login, get_user_info
from backend.modules.session_manager import create_session
from backend.modules.code_generator import get_hash
from backend.entities import regex_config, regex_messages
from backend.entities.forms import LoginForm
from backend.modules.database import cursor, db


@account_bp.post('/login')
@cross_origin()
def user_login_handler():
    browser = request.headers.get('browser')

    if browser is None:
        return dumps({'errorMessage': 'Неверные данные запроса.'}, ensure_ascii=False), 403

    data = request.json

    try:
        form = LoginForm(**data)
    except TypeError:
        return dumps({'errorMessage': 'Недопустимые значения полей. Смотрите документацию.'}, ensure_ascii=False), 400

    user = action_login(password=get_hash(form.password), login=form.login)
    
    if user is None:
        return dumps({'errorMessage': f'Аккаунт с именем пользователя, почтой или паролем не найден.'}, ensure_ascii=False), 400

    user_info = get_user_info(user)

    if user_info is None:
        return dumps({'errorMessage': 'Дополнительная иформация об аккаунте не найдена.'}, ensure_ascii=False), 400

    return dumps({**asdict(user_info), 'token': create_session(user, browser, request.remote_addr)},
                 ensure_ascii=False,
                 default=str), 200


@account_bp.get('/login/check')
@cross_origin()
def user_login_check():
    login = request.args.get('login').strip().lower()

    try:
        cursor.execute("SELECT id FROM users WHERE login = %s", (login,))
    except Exception as e:
        db.rollback()

        error(f'DATABASE ERROR ON CHECK_LOGIN: {e}')
        return dumps({'errorMessage': 'Во время запроса произошла ошибка, повторите попытку позже.'},
                     ensure_ascii=False), 500

    user_id = cursor.fetchone()

    msg = 'занят'
    if is_login_available := user_id is None:
        msg = 'свободен'
    return dumps({'message': f'Логин {login} {msg}.', 'is_login_available': is_login_available},
                 ensure_ascii=False), 500
