from main import addition, subtraction, newfunction, pwdgen
import string

def test_pwdgen_strong_length():
    """Test if the length of strong passwords match"""
    assert 8 <= len(pwdgen("strong")) <= 12


def test_pwdgen_weak_length():
    """Test if the length of weak passwords match"""
    assert 6 <= len(pwdgen("weak")) <= 8


def test_pwdgen_strong_consecutive_lower():
    """Test if there are consecutive or duplicate symbols in strong passwords"""
    assert [
        0
        for i, j in enumerate(sorted(pwdgen("strong").lower())[:-1])
        if j == sorted(pwdgen("strong").lower())[i + 1]
    ] != [0]


def test_pwdgen_weak_consecutive_lower():
    """Test if there are consecutive or duplicate symbols in weak passwords"""
    assert [
        0
        for i, j in enumerate(pwdgen("weak").lower()[:-1])
        if j == pwdgen("weak").lower()[i + 1]
    ] != [0]


def test_pwdgen_strong_symbols_duplicates():
    """Test if there are symbols in strong passwords"""
    assert len([i for i in pwdgen("strong") if i in string.punctuation]) != 0


def test_pwdgen_weak_symbols():
    """Test if there are symbols in weak passwords"""
    assert len([i for i in pwdgen("weak") if i not in string.punctuation]) == len(
        pwdgen("weak")
    )


def test_pwdgen_weak_symbols():
    """Test if there are symbols in weak passwords"""
    assert len([i for i in pwdgen("weak") if i not in string.punctuation]) == len(
        pwdgen("weak")
    )
