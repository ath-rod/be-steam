from string import ascii_letters, digits
from random import choices


def random_str(len: int = 25) -> str:
    chars = [char for char in ascii_letters + digits]
    return "".join(choices(chars, k=len))
