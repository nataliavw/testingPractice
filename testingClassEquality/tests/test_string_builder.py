from lib.string_builder import *

def test_single_addition():
    string = StringBuilder()
    string.add("hello")
    result = string.output()
    assert result == "hello"

def test_single_addition_length():
    string = StringBuilder()
    string.add("hello")
    result = string.size()
    assert result == 5

def test_double_addition():
    string = StringBuilder()
    string.add("hello")
    string.add("there")
    result = string.output()
    assert result == "hellothere"

def test_double_addition_length():
    string = StringBuilder()
    string.add("hello")
    string.add("there")
    result = string.size()
    assert result == 10