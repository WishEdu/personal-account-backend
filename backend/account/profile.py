from json import dumps
from dataclasses import asdict

from . import account_bp
from backend.authentification import access_handler
from backend.modules.user import get_user_info


@account_bp.get('/me')
@access_handler()
def profile_handler(user):
    full_info = get_user_info(user)
    return dumps(asdict(full_info), ensure_ascii=False, default=str), 200
