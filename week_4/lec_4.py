"""
*** library ***

-> import 
# imports a code/module/library

import random

#now you have access to random.py modules e.g:

import random
print(random.randint(0,1))

->from
#when you wanna import some modules of that library but not all

from random import randint
print(randint(0,1))

*** built-in modules ***

-> random

a library which has randint() 
and gives you a power to play with randomness

### randint(a : int , b : int) 
#Return random integer in range [a, b], including both end points.

### choice(seq)
#Choose a random element from a non-empty sequence.

### shuffle(seq)
# shuffles the list (or anythin) IN PLACE and returns NONE

l=[1,2,3,4,5,6,7,8,9,11,22,33,44]
random.shuffle(l)
print(l)

"""



#watched till minute 17 (before statistics library)