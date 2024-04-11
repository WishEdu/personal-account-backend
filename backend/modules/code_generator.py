from random import choices
from string import ascii_letters
from hashlib import sha256
from hmac import new


def get_code(length: int = 4) -> str:
    return ''.join(choices(ascii_letters, k=length))


def get_hash(string):
    return new(
        key=b'WISH-personal-account',
        msg=string.encode(),
        digestmod=sha256
    ).hexdigest()
