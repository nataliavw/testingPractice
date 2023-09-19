from lib.gratitudes import *

def test_single_gratitude():
    gratitude = Gratitudes()
    gratitude.add("coding")
    result = gratitude.format()
    assert result == "Be grateful for: coding"

def test_two_gratitudes():
    gratitude = Gratitudes()
    gratitude.add("coding")
    gratitude.add("crochet")
    result = gratitude.format()
    assert result == "Be grateful for: coding, crochet"

def test_three_gratitudes():
    gratitude = Gratitudes()
    gratitude.add("coding")
    gratitude.add("crochet")
    gratitude.add("cats")
    result = gratitude.format()
    assert result == "Be grateful for: coding, crochet, cats"