from backend import app
from flask import Flask, request
from flask_mail import Mail, Message
from backend.email import email
from flask_cors import cross_origin


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'rutwishedu@gmail.com'  # введите свой адрес электронной почты здесь
app.config['MAIL_DEFAULT_SENDER'] = 'rutwishedu@gmail.com'  # и здесь
app.config['MAIL_PASSWORD'] = 'b352qeda46EW'  # введите пароль
app.config['SECRET_KEY'] = 'kmafpliuruappqfh'
mail = Mail(app)


@email.post('/send')
@cross_origin()
def test():
    msg = Message(
        'TEST',
        sender='noreply@demo.com',
        recipients = ['ivid09390@gmail.com']
    )
    msg.body = 'test'
    mail.send(msg)
    return 'SENT EMAIL'