from plates import is_valid

def test_first_law():
    assert is_valid("1AA")==False
    assert is_valid("!AA")==False
    assert is_valid("A11")==False
    assert is_valid("111")==False
    assert is_valid(" AA")==False
def test_second_law():
    assert is_valid("AAAAAAA")==False
    assert is_valid("AA11111")==False
    assert is_valid("A")==False
    assert is_valid("1")==False
    assert is_valid("50")==False
def test_third_law1():
    assert is_valid("AA0")==False
    assert is_valid("AA0111")==False
    assert is_valid("AA0AAA")==False
    assert is_valid("AA1AAA")==False
    assert is_valid("AA111A")==False
def test_fourth_law():
    assert is_valid("AA.")==False
    assert is_valid("AA!")==False
    assert is_valid("AA A")==False
    assert is_valid("AA,")==False
    assert is_valid("AA,A")==False
    assert is_valid("! AA")==False

def test_acceptables():
    assert is_valid("AA")==True
    assert is_valid("AB")==True
    assert is_valid("AA1234")==True
    assert is_valid("AAAAAA")==True
    assert is_valid("AAA123")==True
    assert is_valid("AA12")==True
    assert is_valid("AA10")==True
    assert is_valid("AA200")==True