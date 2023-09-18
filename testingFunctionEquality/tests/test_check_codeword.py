from lib.check_codeword import *

def test_check_correct_when_horse():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_check_close_when_home():
    result = check_codeword("home")
    assert result == "Close, but nope."

def test_check_incorrect_when_hand():
    result = check_codeword("hand")
    assert result == "WRONG!"