from lib.report_length import *

def test_string_is_four_chars_long():
    result = report_length("four")
    assert result == "This string was 4 characters long."

def test_string_is_fifteen_chars_long():
    result = report_length("done and dusted")
    assert result == "This string was 15 characters long."

def test_string_is_two_chars_long():
    result = report_length("no")
    assert result == "This string was 2 characters long."

def test_string_is_zero_chars_long():
    result = report_length("")
    assert result == "This string was 0 characters long."