from datetime import datetime
from hashlib import sha256
from backend import app
from flask import Flask, request
from flask_mail import Mail, Message
from backend.email import email_blueprint
from flask_cors import cross_origin
from backend.modules.database import cursor, db



app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'rutwishedu@gmail.com'  # введите свой адрес электронной почты здесь
app.config['MAIL_DEFAULT_SENDER'] = 'rutwishedu@gmail.com'  # и здесь
app.config['MAIL_PASSWORD'] = 'kmafpliuruappqfh'  # введите пароль

mail = Mail(app)



def create_unique_id(email) -> str:
    return str(hex(int(datetime.now().timestamp())))[2:] + sha256(email.encode(encoding="utf-8")).hexdigest()
    

@email_blueprint.post('/send')
@cross_origin()
def send_mail():
    email_name = request.json['email_name']
    user_id = request.json['user_id']
    hash_ = create_unique_id(email_name)
    cursor.execute('''
        INSERT INTO email_confirm VALUES (%s, %s);
    ''', (user_id, hash_))
    db.commit()
    msg = Message(
        'TEST',
        sender='rutwishedu@gmail.com',
        recipients = [email_name]
    )
    msg.body = 'test'
    mail.send(msg)
    return hash_

@email_blueprint.get('/confirm')
@cross_origin()
def test():
    hash_ = request.args['hash']
    cursor.execute("""
        SELECT user_id FROM email_confirm
        WHERE hash = %s
    """, (hash_,))
    data = cursor.fetchone()
    if data is None:
        return 'No such email to confirm'
    cursor.execute("""
        UPDATE users 
        SET is_confirmed = TRUE
        WHERE id = %s
    """, (data['user_id'],))
    db.commit()
    return 'SENT EMAIL'