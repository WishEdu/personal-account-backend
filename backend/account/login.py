from dataclasses import asdict
from flask import request
from json import dumps

from . import account_bp

from backend.modules.user import get_user
from backend.modules.session_manager import create_session
from backend.modules.code_generator import get_hash
from backend.entities.forms import LoginForm


@account_bp.post('/login')
def user_login_handler():
    browser = request.headers.get('browser')

    if browser is None:
        return dumps({'errorMessage': 'Неверные данные запроса.'}, ensure_ascii=False), 403

    data = request.json

    try:
        form = LoginForm(**data)
    except TypeError:
        return dumps({'errorMessage': 'Недопустимые значения полей. Смотрите документацию.'}, ensure_ascii=False), 400

    is_valid = form.get_validation
    if not is_valid and len(data) < 2:
        return dumps(is_valid), 400

    auth = form.auth
    user = get_user(password=get_hash(form.password), **{auth[0]: auth[1]})

    if user is None:
        return dumps({'errorMessage': 'Аккаунт не найден.'}, ensure_ascii=False), 400

    return dumps({**asdict(user), 'token': create_session(user, browser, request.remote_addr)}, ensure_ascii=False,
                 default=str), 200
