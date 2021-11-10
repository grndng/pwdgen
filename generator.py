from random import randint, sample
import string

alphabet = string.ascii_letters
digits = string.digits
symbols = string.punctuation
no_whitespace = string.printable.strip()

def pwdgen(strength: str) -> str:
    strength = strength.lower()
    pwd = ""
    if strength == "strong":
        length = randint(8,12)
        pwd = sample(no_whitespace, length)
        return "".join(pwd)
    
    
    elif strength == "weak":
        return "a5afah"

print(pwdgen("Strong"))