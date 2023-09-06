
from um import count


def test_not_valid():
    assert count("a yummy a")==0
    assert count("ummy a")==0
    assert count("umy a ummy umd")==0
    assert count(",ummy")==0
    assert count(",ummy,")==0
    assert count("yummyum,")==0

def test_correct_num():
    assert count("!@#$%^&*.,um&*.,")==1
    assert count("um um um")==3
    assert count(",um .um.um")==3
    assert count("im ummy um, yummy um um ")==3
    assert count("ummy um")==1
    assert count("yummyumm")==0

def test_case():
    assert count("!@#$%^&*.,UM&*.,")==1
    assert count("UM UM UM")==3
    assert count(",um .um.um")==3
    assert count("im ummy UM, YUMMY um um ")==3
    assert count("ummy. UM,")==1
    assert count("yUMMY")==0