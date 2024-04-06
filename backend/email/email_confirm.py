from hashlib import sha256
from datetime import datetime
from json import dumps
from os import getenv


from dotenv import load_dotenv
from flask import request, url_for, redirect
from flask_mail import Message
from flask_cors import cross_origin
from logging import error

from . import mail
from backend.email import email_bp
from backend.modules.database import cursor, db
from backend.entities.forms import ConfirmEmailForm
from backend.modules.create_mail import generate_mail
from backend.modules.user import get_user

load_dotenv()


def create_unique_id(email) -> str:
    return str(hex(int(datetime.now().timestamp())))[2:] + sha256(email.encode(encoding="utf-8")).hexdigest()
    

@email_bp.post('/confirm-send')
@cross_origin()
def send_confirm_mail_handler():
    data = request.json
    try:
        form = ConfirmEmailForm(**data)
    except TypeError:
        return dumps({'errorMessage': 'Недопустимые значения полей. Смотрите документацию.'}, ensure_ascii=False), 400
    
    is_valid = form.get_validation
    if not is_valid:
        return dumps(is_valid, ensure_ascii=False), 400
    
    hash_ = create_unique_id(form.email)
    try:
        cursor.execute('INSERT INTO email_confirm VALUES (%s, %s);', (form.user_id, hash_))
    except Exception as e:
        error(f'ERROR: {e}')
        db.rollback()
        return dumps({'errorMessage': 'Произошла ошибка базы данных'}, ensure_ascii=False), 500
    db.commit()
    msg = Message(
        'Подтвердите учетную запись',
        sender=getenv('SENDER_NAME'),
        recipients = [form.email]
    )
    user = get_user(id = form.user_id)
    msg.html = generate_mail(user.login, url=f"{request.host_url[:-1]}{url_for('email.confirm_mail_handler', hash=hash_ )}")
    mail.send(msg)
    return dumps({'status': True}, ensure_ascii=False), 200


@email_bp.get('/confirm')
@cross_origin()
def confirm_mail_handler():
    
    hash_ = request.args.get('hash')
    cursor.execute("""
        SELECT user_id FROM email_confirm
        WHERE hash = %s
    """, (hash_,))
    data = cursor.fetchone()
    if data is None:
        return dumps({'errorMessage': 'Некорректный код подтверждения'}, ensure_ascii=False), 400
    try:
        cursor.execute("""
            UPDATE users 
            SET is_confirmed = TRUE
            WHERE id = %s
        """, (data['user_id'],))
    except Exception as e:
        error(f'ERROR: {e}')
        db.rollback()
        return dumps({'errorMessage': 'Произошла ошибка базы данных'}, ensure_ascii=False), 500

    db.commit()
    return redirect(getenv('FRONTEND_HOST'))