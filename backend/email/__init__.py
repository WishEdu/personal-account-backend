from flask import Blueprint
from flask_mail import Mail

from backend import app
from backend.configs import MAIL_USERNAME, MAIL_PASSWORD


email_bp = Blueprint('email', __name__, url_prefix='/email')

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = MAIL_USERNAME
app.config['MAIL_DEFAULT_SENDER'] = MAIL_USERNAME
app.config['MAIL_PASSWORD'] = MAIL_PASSWORD

mail = Mail(app)

from .email_confirm import send_confirm_mail_handler, confirm_mail_handler

