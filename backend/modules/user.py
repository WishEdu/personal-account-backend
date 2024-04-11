from logging import error, info
from typing import Optional
from datetime import datetime
from dataclasses import fields, astuple, asdict
from json import dumps

from backend.modules.database import cursor, db
from backend.entities.user import User, Group, Role
from backend.entities.forms import UserEditForm



def get_user_permissions(user_id):
    cursor.execute(
        """SELECT p.name FROM permissions p
        INNER JOIN users_permissions up ON p.id = up.permission_id AND up.user_id = %s
        UNION DISTINCT
        SELECT p.name FROM permissions p
        INNER JOIN roles_permissions rp ON p.id = rp.permission_id 
        and rp.role_id IN (SELECT ur.role_id FROM users_roles ur WHERE ur.user_id = %s)
        """,
        (user_id, user_id)
    )
    return cursor.fetchall()


def get_user_info(user: User = None):
    if user is None:
        return None

    cursor.execute(
        f"""SELECT g.id, g.name
        FROM groups g 
        INNER JOIN users_groups ug ON ug.group_id = g.id AND ug.user_id = %s""",
        (user.id,))

    user.groups = [Group(**group) for group in cursor.fetchall()]

    cursor.execute(
        f"""SELECT r.id, r.name
        FROM roles r 
        INNER JOIN users_roles ur ON r.id = ur.role_id AND ur.user_id = %s""",
        (user.id,)
    )

    user.roles = [Role(**role) for role in cursor.fetchall()]

    user.permissions = [permission['name'] for permission in get_user_permissions(user.id)]
    return user


def get_user(sep='AND', **kwargs):
    build_sql = f' {sep} '.join([f"{key}=%s" for key in kwargs])
    cursor.execute(
        f"SELECT {', '.join((f.name for f in fields(User) if f.type in (str, int, datetime, Optional[str], Optional[int])))} FROM users WHERE {build_sql}",
        (*kwargs.values(),))
    row = cursor.fetchone()

    if row is None:
        return None

    return User(**row)


def action_login(login, password):
    cursor.execute(
        f"SELECT {', '.join((f.name for f in fields(User) if f.type in (str, int, datetime, Optional[str], Optional[int])))} FROM users WHERE password = %s AND (login = %s OR email = %s)",
        (password, login, login))
    row = cursor.fetchone()

    if row is None:
        return None

    return User(**row)


def user_edit(data, user_id):
    try:
        form = UserEditForm(**data)
    except TypeError:
        return dumps({'errorMessage': 'Недопустимые значения полей. Смотрите документацию.'}, ensure_ascii=False), 400

    is_valid = form.get_validation

    if is_valid is not True:
        return dumps(is_valid, ensure_ascii=False), 400

    q = f"UPDATE users SET {', '.join([f'{f.name}=%s' for f in fields(form)])} WHERE id = %s"
    info(q)
    try:
        cursor.execute(q,
                       (*astuple(form), user_id))
    except Exception as e:
        db.rollback()

        error(f'DATABASE ERROR ON EDIT_ACCOUNT: {e}')
        return dumps({'errorMessage': 'Во время запроса произошла ошибка, повторите попытку позже.'},
                     ensure_ascii=False), 500

    db.commit()
    return dumps(asdict(form), ensure_ascii=False), 200


def get_users():
    cursor.execute(
        f"SELECT {', '.join((f.name for f in fields(User) if f.type in (str, int, datetime, Optional[str], Optional[int])))} FROM users ORDER BY id")
    rows = cursor.fetchall()

    users = []
    for row in rows:
        user = User(**row)
        cursor.execute(
            f"""SELECT g.id, g.name
                FROM groups g 
                INNER JOIN users_groups ug ON ug.group_id = g.id AND ug.user_id = %s""",
            (user.id,))

        user.groups = [Group(**group) for group in cursor.fetchall()]

        cursor.execute(
            f"""SELECT r.id, r.name
                FROM roles r 
                INNER JOIN users_roles ur ON r.id = ur.role_id AND ur.user_id = %s""",
            (user.id,)
        )

        user.roles = [Role(**role) for role in cursor.fetchall()]

        user = asdict(user)
        del user['permissions']
        users.append(user)

    return users
