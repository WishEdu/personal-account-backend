from os import getenv
from typing import Optional
from datetime import datetime
from dataclasses import fields
from dotenv import load_dotenv

from backend.modules.database import cursor
from backend.entities.user import User, Group, Role

load_dotenv()


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
