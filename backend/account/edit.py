from flask import Blueprint, request
from . import account_bp
from backend.authentification import access_handler
from backend.modules.user import user_edit

user_edit_bp = Blueprint('user_edit', __name__, url_prefix='/edit')


@user_edit_bp.post('/info')
@access_handler()
def user_edit_handler(user):
    return user_edit(request.json, user.id)


account_bp.register_blueprint(user_edit_bp)