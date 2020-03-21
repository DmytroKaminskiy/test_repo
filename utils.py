import random
import string


def generate(num: int = 0) -> str:
    """
    :param num: password length
    :return: string
    """
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join([random.choice(chars) for _ in range(num)])
    return password
