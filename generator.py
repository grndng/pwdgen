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
        return "1a2!s3d4f"
    
    
    elif strength == "weak":
        return "a5afah"

print(any(symbol in pwdgen("Strong") for symbol in symbols))
