"""generator_test.py

Testfile for generator.py: Simply tests my made up 
requirements for what a strong and weak password 
should look like.
"""

from generator import pwdgen
import string


def test_pwdgen_strong_length():
    """Test if the length of strong passwords match"""
    print(pwdgen("strong"))
    assert 8 <= len(pwdgen("strong")) <= 12


def test_pwdgen_weak_length():
    """Test if the length of weak passwords match"""
    assert 6 <= len(pwdgen("weak")) <= 8


def test_pwdgen_strong_consecutive_lower():
    """Test if there are consecutive or duplicate symbols in strong passwords"""
    pwd = "".join(sorted(pwdgen("strong"))).lower()
    assert [0 for i, j in enumerate(pwd[:-1]) if pwd[i] == pwd[i + 1]] != [0]


def test_pwdgen_weak_consecutive_lower():
    """Test if there are consecutive symbols in weak passwords"""
    pwd = pwdgen("weak").lower()
    assert [0 for i, j in enumerate(pwd[:-1]) if j == pwd[i + 1]] != [0]


def test_pwdgen_strong_symbols_duplicates():
    """Test if there are symbols in strong passwords"""
    pwd = pwdgen("strong")
    assert any(symbol in pwd for symbol in string.punctuation) == True
    # any() is probably faster than iterating around:
    # assert len([i for i in pwdgen("strong") if i in string.punctuation]) != 0


def test_pwdgen_weak_symbols():
    """Test if there are symbols in weak passwords (lazy)"""
    pwd = pwdgen("weak")
    assert any(symbol in pwd for symbol in string.punctuation) == False
    # using any instead of iterating over list:
    # assert len([i for i in pwdgen("weak") if i not in string.punctuation]) == len(
    #    pwdgen("weak")
    # )
    # can also test with re [^A-Za-z0-9]+
