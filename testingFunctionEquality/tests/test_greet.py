from lib.greet import *

def test_greet_returns_alex_for_name():
    result = greet("alex")
    assert result == "Hello, alex!"