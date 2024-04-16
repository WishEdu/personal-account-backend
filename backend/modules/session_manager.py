from hmac import new
from json import dumps
from hashlib import sha256
from datetime import datetime

from logging import error
from backend.modules.database import cursor, db
from backend.modules.code_generator import get_code


def create_session(user, browser, ip):
    token = new(
        key=b'WISH-personal-account',
        msg=f"{user.id}-{user.login}-{datetime.now().timestamp()}-{get_code(6)}".encode(),
        digestmod=sha256
    ).hexdigest()

    try:
        cursor.execute("INSERT INTO sessions (user_id, token, browser_info, ip_address) VALUES (%s, %s, %s, %s) ", (user.id, token, browser, ip))
    except Exception as E:
        db.rollback()
        error(f'Create session DB error: {E} | user_id: {user.id}', exc_info=True)

        return dumps({'errorMessage': 'Ошибка транзакции в базе данных. Сообщите разработчикам.'},
                     ensure_ascii=False), 500

    db.commit()
    return token


def get_user_by_session(token):
    cursor.execute('SELECT user_id FROM sessions WHERE token = %s', (token, ))
    user_id = cursor.fetchone()

    if user_id is None:
        return None

    return user_id['user_id']
