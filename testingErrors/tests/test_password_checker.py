import pytest
from lib.password_checker import *

def test_exception_for_seven_chars():
    checker = PasswordChecker
    with pytest.raises(Exception) as e:
        checker.check(checker, "1234567")
    error = str(e.value)
    assert error == "Invalid password, must be 8+ characters."

def test_pass_for_eight_chars():
    checker = PasswordChecker
    result = checker.check(checker, "12345678")
    assert result == True