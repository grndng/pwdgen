def pwdgen(strength: str) -> str:
    if strength == "strong":
        return "a5f!gw731"
    elif strength == "weak":
        return "a52fah"


import string

alphabet = string.ascii_letters
digits = string.digits
symbols = string.punctuation