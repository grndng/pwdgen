"""Testfile for generator.py

Simply tests my made up requirements for what a strong
and weak password should look like.
"""

from generator import pwdgen
import string


def test_pwdgen_strong_length():
    """Test if the length of strong passwords match"""
    assert 8 <= len(pwdgen("strong")) <= 12


def test_pwdgen_weak_length():
    """Test if the length of weak passwords match"""
    assert 6 <= len(pwdgen("weak")) <= 8


def test_pwdgen_strong_consecutive_lower():
    """Test if there are consecutive or duplicate symbols in strong passwords"""
    print(pwdgen("strong"))
    assert [
        0
        for i, j in enumerate(sorted(pwdgen("strong").lower())[:-1])
        if j == sorted(pwdgen("strong").lower())[i + 1]
    ] != [0]


def test_pwdgen_weak_consecutive_lower():
    """Test if there are consecutive symbols in weak passwords"""
    assert [
        0
        for i, j in enumerate(pwdgen("weak").lower()[:-1])
        if j == pwdgen("weak").lower()[i + 1]
    ] != [0]


def test_pwdgen_strong_symbols_duplicates():
    """Test if there are symbols in strong passwords"""
    assert any(symbol in pwdgen("strong") for symbol in string.punctuation) == True
    # any() is probably faster than iterating around
    # assert len([i for i in pwdgen("strong") if i in string.punctuation]) != 0


def test_pwdgen_weak_symbols():
    """Test if there are symbols in weak passwords"""
    assert any(symbol in pwdgen("weak") for symbol in string.punctuation) == False
    # assert len([i for i in pwdgen("weak") if i not in string.punctuation]) == len(
    #    pwdgen("weak")
    # )