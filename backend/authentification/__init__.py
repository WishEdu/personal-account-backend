from backend import app
from json import dumps
from flask import request as r
from flask_cors import cross_origin
import numpy as np

from backend.modules.session_manager import get_user_by_session
from backend.modules.user import get_user_permissions, get_user


def access_handler(permissions: tuple = ()):
    def handle(func):
        @cross_origin()
        def inner(**kwargs):
            auth_token = r.headers.get('Authorization', '')

            if len(auth_token) != 64:
                return dumps({'errorMessage': 'Undefined token'}, ensure_ascii=False), 403

            user_id = get_user_by_session(auth_token)

            if user_id is None:
                return dumps({'errorMessage': 'Нет доступа!'}, ensure_ascii=False), 403

            if len(permissions) > 0:
                user_permissions = get_user_permissions(user_id)

                have_access = np.intersect1d(user_permissions, permissions)
                if len(have_access) == 0:
                    return dumps({'errorMessage': 'Нет доступа!'}, ensure_ascii=False), 403

            user = get_user(user_id)
            if user is not None:
                return func(user=user, **kwargs)

        inner.__name__ = func.__name__
        return inner

    return handle
