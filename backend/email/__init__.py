from flask import Blueprint
from dotenv import load_dotenv
from backend import app
from os import getenv
from flask_mail import Mail


load_dotenv()



email_bp = Blueprint('email', __name__, url_prefix='/email')

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = getenv('MAIL_USERNAME')  
app.config['MAIL_DEFAULT_SENDER'] = getenv('MAIL_USERNAME')  
app.config['MAIL_PASSWORD'] = getenv('MAIL_PASSWORD')  

mail = Mail(app)

from .email_confirm import send_confirm_mail_handler, confirm_mail_handler

