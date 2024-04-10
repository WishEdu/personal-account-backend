from dataclasses import asdict
from flask import Blueprint, request
from json import dumps
from backend.modules.user import get_users, get_user, get_user_info

users_bp = Blueprint('users', __name__, url_prefix='/users')


@users_bp.get('/')
def users_get_handler():

    return dumps({'users': get_users()}, ensure_ascii=False, default=str), 200


@users_bp.get('/search-<param>')
def user_search(param):
    # TODO доделать регулярку логина, чтобы там нельзя было вписать только цифры

    if param.isdigit():
        user = get_user(id=param)
    else:
        user = get_user(login=param)
    user = asdict(get_user_info(user))
    del user['permissions']
    return dumps(user, ensure_ascii=False, default=str), 200
