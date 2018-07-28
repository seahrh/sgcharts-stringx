__all__ = [
    'to_str',
    'to_bytes',
    'strip_punctuation',
    'to_ascii_str',
    'is_number',
    'count_digit',
    'count_alpha',
    'count_upper',
    'count_space',
    'count_punctuation'
]

import string
from unicodedata import normalize


def to_str(bytes_or_str, encoding='utf-8'):
    """Based on Effective Python Item 3:
    Know the difference between bytes str and unicode
    """
    if isinstance(bytes_or_str, bytes):
        return bytes_or_str.decode(encoding)
    # Instance of str
    return bytes_or_str


def to_bytes(bytes_or_str, encoding='utf-8'):
    """Based on Effective Python Item 3:
    Know the difference between bytes str and unicode
    """
    if isinstance(bytes_or_str, str):
        return bytes_or_str.encode(encoding)
    # Instance of bytes
    return bytes_or_str


def strip_punctuation(s):
    """This uses the 3-argument version of str.maketrans with arguments (x, y, z) where 'x' and 'y'
    must be equal-length strings and characters in 'x'
    are replaced by characters in 'y'. 'z'
    is a string (string.punctuation here)
    where each character in the string is mapped
    to None
    translator = str.maketrans('', '', string.punctuation)

    This is an alternative that creates a dictionary mapping
    of every character from string.punctuation to None (this will
    also work)

    Based on https://stackoverflow.com/a/34294398/519951
    """
    translator = str.maketrans(dict.fromkeys(string.punctuation))
    return s.translate(translator)


def to_ascii_str(u):
    """Normalise (normalize) unicode data in Python to remove umlauts, accents etc.

    Based on https://gist.github.com/j4mie/557354
    """
    return to_str(normalize("NFKD", u).encode('ASCII', 'ignore'))


def is_number(s):
    """Based on https://stackoverflow.com/a/40097699/519951

    :param s: string
    :return: True if string is a number
    """
    res = True
    try:
        num = float(s)
        # check for "nan" floats
        res = num == num   # or use `math.isnan(num)`
    except ValueError:
        res = False
    return res


def count_digit(s):
    n = 0
    for c in s:
        if c.isdigit():
            n += 1
    return n


def count_alpha(s):
    n = 0
    for c in s:
        if c.isalpha():
            n += 1
    return n


def count_upper(s):
    n = 0
    for c in s:
        if c.isupper():
            n += 1
    return n


def count_space(s):
    n = 0
    for c in s:
        if c.isspace():
            n += 1
    return n


def count_punctuation(s):
    n = 0
    for c in s:
        if c in string.punctuation:
            n += 1
    return n
