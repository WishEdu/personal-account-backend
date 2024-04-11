from json import dumps
from flask import request as r
from flask_cors import cross_origin

from backend.modules.session_manager import get_user_by_session
from backend.modules.user import get_user_permissions, get_user


def access_handler(permission: str | None = None):
    def handle(func):
        @cross_origin()
        def inner(**kwargs):
            auth_token = r.headers.get('Authorization', '')

            if len(auth_token) != 64:
                return dumps({'errorMessage': 'Undefined token'}, ensure_ascii=False), 403

            user_id = get_user_by_session(auth_token)

            if user_id is None:
                return dumps({'errorMessage': 'Нет доступа!'}, ensure_ascii=False), 403

            if permission is not None:
                user_permissions = get_user_permissions(user_id)

                have_access = permission in user_permissions
                if not have_access:
                    return dumps({'errorMessage': 'Нет доступа!'}, ensure_ascii=False), 403

            user = get_user(id=user_id)
            if user is not None:
                return func(user=user, **kwargs)

        inner.__name__ = func.__name__
        return inner

    return handle
