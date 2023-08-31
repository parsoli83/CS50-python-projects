
"""
def test_normal():
    assert value("hello")==0
    assert value("hello , world")==0
    assert value("Hello")==0
    assert value("HELLO WORLD")==0
    assert value("Hello0123.,?!")==0
    assert value("HI WORLD")==20
    assert value("hi world")==20
    assert value("h ello")==20
    assert value("has dfgh j")==20
    assert value("HAsdfghj")==20
    assert value("hasdfghj")==20
    assert value("What’s up")==100
    assert value("wassup world") == 100
    assert value("WASSUP WORLD") == 100
    assert value("asdf")==100
"""
from bank import value


def test_greetings():
    assert value("hello worldi") == 0
    assert value("HELLO WORLDi") == 0
    assert value("hi worldi") == 20
    assert value("HI WORLDi") == 20
    assert value("wassup worlid") == 100
    assert value("WASSUP WORLDi") == 100