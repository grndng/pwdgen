"""generator.py

The generator part of the password generator. Overall it would
work much easier with regex (https://regexr.com/ saves lives).
"""

from random import randint, sample, shuffle
import string
import re

alphabet = string.ascii_letters
digits = string.digits
weakpw = string.ascii_letters + string.digits
symbols = string.punctuation
no_whitespace = string.printable.strip()


def pwdgen(strength: str) -> str:
    """Sloppy password generator that creates passwords based
    on randomly thought out criteria.

    Parameters:
            strength (str): Expects "strong" or "weak"

    Returns:
            pwd (str): Returns the password

    """
    strength = strength.lower()
    pwd = "00"
    if strength == "strong":
        while len(set(pwd.lower())) != len(pwd.lower()):
            pwd = mandatory_strong()
            pwd += "".join(sample(no_whitespace, randint(4, 8)))
        pwd = list(pwd)
        shuffle(pwd)
        return "".join(pwd)
    elif strength == "weak":
        while len(re.findall(r"(?=[a-zA-Z0-9])([a-zA-Z0-9])\1{1,}", pwd.lower())) != 0:
            pwd = ""
            pwd += "".join(sample(weakpw, randint(6, 8)))
        return pwd


def mandatory_strong() -> str:
    """Small utility to:
        - reset the password in case there are duplicates caught by the
        length-comparison in the while loop of pwdgen()

        - fill up the string with the mandatory elements set for strong
        passwords (symbol, upper- and lowercase letter, digit)

    Parameters:
            None

    Returns:
            pwd (str): Returns

    """
    # TODO: concatenate string in a simpler fashion
    pwd = ""
    pwd += "".join(sample(alphabet[:26], 1))
    pwd += "".join(sample(alphabet[26:], 1))
    pwd += "".join(sample(digits, 1))
    pwd += "".join(sample(symbols, 1))
    return pwd
