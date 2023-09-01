from fuel import convert
from fuel import gauge
import pytest

def test_convert():
    # zero division error
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("cat/0")
    # ValueError
    with pytest.raises(ValueError):
        convert("1/")
    with pytest.raises(ValueError):
        convert("/1")
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("cat/1")
    with pytest.raises(ValueError):
        convert("1/cat")
    assert convert("3/7")==43
    assert convert("2/6")==33
    assert convert("1/6")==17
    assert convert("4/9")==44
    assert convert("1/1")==100
    assert convert("0/1")==0
    
def test_gauge():
    assert gauge(0)=="E"
    assert gauge(0.5)=="E"
    assert gauge(1)=="E"
    assert gauge(99)=="F"
    assert gauge(99.5)=="F"
    assert gauge(100)=="F"
    assert gauge(10)==f"{10}%"
    assert gauge(20)==f"{20}%"
    assert gauge(30)==f"{30}%"
    

    
    