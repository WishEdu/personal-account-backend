from random import choices
from string import ascii_letters


def get_code(length: int = 4) -> str:
    return ''.join(choices(ascii_letters, k=length))
