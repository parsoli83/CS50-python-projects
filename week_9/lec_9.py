"""
*** type hints ***
# making a var with static type

def meow(n:int):
#n should be an int

n:int=value
#this works too

*** docstring ***
documenting


*** unpacking ***

def func (a,b,c):
    ...

l=[a,b,c]
func(*l)

coins={
    a:"a",
    "b":b,
    "c":c
}
func(**coins)

*** map ***

map(function,iterable)
filter(is_upper,iterable)
sorted(iterable,key)

eg:

l=["a","b","c"]
map(str.upper,l)
# l=["A","B","C"]

*** list comprehension ***

l=["a","b","c"]
uppered=[letter.upper() for letter in l]
# l=["A","B","C"]

l=["a","b","c"]
letters=[{
    "letter":letter,"type": "int"
} for letter in l
]

letters_dic={
    letter_type: "lower"
} for letter in l

"""
