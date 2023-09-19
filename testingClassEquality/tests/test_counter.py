from lib.counter import *

def test_counts_to_four():
    counter = Counter()
    counter.add(4)
    result = counter.report()
    assert result == "Counted to 4 so far."

def test_counts_to_five_two_jumps():
    counter = Counter()
    counter.add(3)
    counter.add(2)
    result = counter.report()
    assert result == "Counted to 5 so far."

def test_subtracts():
    counter = Counter()
    counter.add(5)
    counter.add(-1)
    result = counter.report()
    assert result == "Counted to 4 so far."