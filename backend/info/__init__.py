from flask import Blueprint

info_bp = Blueprint('info', __name__, url_prefix='/info')

from .users import users_bp
info_bp.register_blueprint(users_bp)