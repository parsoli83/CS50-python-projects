"""
*** Unit Test ***

--> assert
#to make an statement for checking code

def power(n):
    return n+n  #yes, a typo

assert power(2)==4
assert power(3)==9

#when you run it:

 File "/home/parsoli/CS50-python-projects/lec_5.py", line 21, in <module>
    assert power(3)==9
AssertionError

#it shows which assert in which line went wrong
# try/except works with AssertionError too


*** pytest ***
# a library for testing code

import pytest
def power(n):
    return n-n  #yes, a typo
assert power(2)==4
assert power(3)==9
assert power(-2)==4
assert power(-3)==9
assert power(0)==0
assert power(1)==1

>>>pytest lec_5.py
============================================== test session starts ===============================================
platform linux -- Python 3.10.6, pytest-7.4.0, pluggy-1.3.0
rootdir: /home/parsoli/CS50-python-projects
collected 0 items / 1 error                                                                                      

===================================================== ERRORS =====================================================
___________________________________________ ERROR collecting lec_5.py ____________________________________________
../.local/lib/python3.10/site-packages/_pytest/assertion/rewrite.py:178: in exec_module
    exec(co, module.__dict__)
lec_5.py:45: in <module>
    assert power(2)==4
E   assert 0 == 4
E    +  where 0 = <function power at 0x7f0fe6982170>(2)
============================================ short test summary info =============================================
ERROR lec_5.py - assert 0 == 4
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
================================================ 1 error in 0.13s ================================================

# and yeah... thats a pretty good description 

#this is possible too


with pytest.raises(TypeError):
    square("cat")

# if square("cat"), raise the error

"""