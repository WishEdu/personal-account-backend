from flask import Blueprint

account_bp = Blueprint('account', __name__, url_prefix='/account')

from .login import user_login_handler
from .registration import registration_handler
from .profile import profile_handler