from random import randint, sample, shuffle
import string

alphabet = string.ascii_letters
digits = string.digits
symbols = string.punctuation
no_whitespace = string.printable.strip()


def pwdgen(strength: str) -> str:
    strength = strength.lower()

    pwd = "00"

    if strength == "strong":
        while len(set(pwd.lower())) != len(pwd.lower()):
            pwd = mandatory_strong()
            pwd += "".join(sample(no_whitespace, randint(4, 8)))
        pwd = list(pwd)
        shuffle(pwd)
        print(f'Returning {"".join(pwd)}')
        return "".join(pwd)

    elif strength == "weak":

        return "a5afah"


def mandatory_strong() -> str:
    """Small utility to:
        - reset the password in case there are duplicates caught by the length-comparison in the while loop of pwdgen()
        - fill up the string with the mandatory elements set for strong passwords (symbol, upper- and lowercase letter, digit)

    Parameters:
            None

    Returns:
            pwd (str): Returns

    """
    #TODO: concatenate string in a simpler fashion

    pwd = ""
    pwd += "".join(sample(alphabet[:26], 1))
    pwd += "".join(sample(alphabet[26:], 1))
    pwd += "".join(sample(digits, 1))
    pwd += "".join(sample(symbols, 1))
    return pwd


print(mandatory_strong.__doc__)
