from flask import Blueprint

email_blueprint = Blueprint('email', __name__, url_prefix='/email')

from .email import send_mail