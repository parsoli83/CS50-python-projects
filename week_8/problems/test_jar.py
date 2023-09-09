from jar import Jar
from pytest import raises

def test_init():
    with raises(ValueError):
        jar=Jar(-1)
    with raises(ValueError):
        jar=Jar("-1")
    jar=Jar()
    assert jar.capacity==12
    jar=Jar(3)
    assert jar.capacity==3


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪🍪"
    jar.withdraw(2)
    assert str(jar) == "🍪🍪"
    jar.withdraw(2)
    assert str(jar) == ""



def test_deposit():
    jar = Jar(3)
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(1)
    assert str(jar) == "🍪🍪"
    jar.deposit(1)
    assert str(jar) == "🍪🍪🍪"
    with raises(ValueError):
        jar.deposit(1)


def test_withdraw():
    jar=Jar(3)
    jar.deposit(3)
    jar.withdraw(1)
    assert jar.cookies==2
    jar.withdraw(2)
    assert jar.cookies==0
    with raises(ValueError):
        jar.withdraw(1)


