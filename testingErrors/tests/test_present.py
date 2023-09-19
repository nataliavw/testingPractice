import pytest
from lib.present import *

def test_content_already_wrapped():
    present = Present()
    present.wrap("content")
    with pytest.raises(Exception) as e:
        present.wrap("second contents")
    error = str(e.value)
    assert error == "A contents has already been wrapped."

def test_content_unwraps():
    present = Present()
    present.wrap("content")
    result = present.unwrap()
    assert result == "content"

def test_no_content_unwrapped():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error = str(e.value)
    assert error == "No contents have been wrapped."