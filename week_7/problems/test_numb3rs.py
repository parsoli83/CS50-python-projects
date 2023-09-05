from numb3rs import validate

def test_validate_struc():
    assert validate("11")==False
    assert validate("11.11")==False
    assert validate("11.11.11")==False
    assert validate("11.11.11.11")==True
    assert validate("11.11.11.11.11")==False
    assert validate("1/1.1.1")==False
    assert validate("1,1.1.1")==False
    assert validate("1-1.1.1")==False

def test_validate_num():
    assert validate("1111.1.1.1")==False
    assert validate("1.1111.1.1")==False
    assert validate("1.1.1111.1")==False
    assert validate("1.1.1.1111")==False
    assert validate("256.1.1.1")==False
    assert validate("1.-1.1.1")==False
    assert validate("1.1.300.1")==False
    assert validate("1.1.1.1")==True
    assert validate("0.1.1.1")==True
    assert validate("255.1.1.1")==True
    assert validate("0.111.200.255")==True
    assert validate("100.200.0.255")==True
