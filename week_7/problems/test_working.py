from working import convert
from pytest import raises
def test_min():
    assert convert("9 AM to 5:30 PM")=="09:00 to 17:30"
    assert convert("9:00 AM to 5:30 PM")=="09:00 to 17:30"
    assert convert("9 PM to 5:30 AM")=="21:00 to 05:30"
    assert convert("9:12 AM to 5:33 PM")=="09:12 to 17:33"
    assert convert("9 AM to 5 PM")=="09:00 to 17:00"
    assert convert("9:12 PM to 10:30 PM")=="21:12 to 22:30"
    assert convert("9:12 AM to 10 AM")=="09:12 to 10:00"

def test_mix():
    assert convert("10 AM to 5 PM")=="10:00 to 17:00"
    assert convert("10:12 PM to 10:30 PM")=="22:12 to 22:30"
    assert convert("10:12 AM to 10 AM")=="10:12 to 10:00"

def test_value_num():
    with raises(ValueError):
        convert("13 AM to 5 PM")
    with raises(ValueError):
        convert("1 AM to 15 PM")
    with raises(ValueError):
        convert("1:60 AM to 5 PM")
    with raises(ValueError):
        convert("1 AM to 5:70 PM")
    with raises(ValueError):
        convert("1  AM to 5 PM")
    with raises(ValueError):
        convert("1 AM to 5  PM")
    with raises(ValueError):
        convert("1 AM  to 5 PM")
    with raises(ValueError):
        convert("1 A to 5 PM")
    with raises(ValueError):
        convert("1 AM to 5 P")
    with raises(ValueError):
        convert("1 AMm to 5 PM")
    with raises(ValueError):
        convert("1 A M to 5 PM")
    with raises(ValueError):
        convert("1 AM to 5 P M")
    with raises(ValueError):
        convert("1 AM  5 PM")
    with raises(ValueError):
        convert("1 AM 5 PM")

