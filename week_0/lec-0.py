"""
print( *objects, sep=" ", end="\n")

$print("hello")
hello

$print("hello"+"world")
helloworld

$print("hello","world")
hello world

$print("hello","world", sep="!!!")
hello!!!world

print("hello", end="")
print("world")
helloworld
"""

# the string can extra space or a , after it

#input function didnt have many things about it in python documents

"""

\n => go to next line or line breaker
\" => literall " as a string

like:

$print("hello \"mr.soli\"")
hello "mr.soli"

it can be done like:

$print('hello "mr.soli"')
hello "mr.soli"

***FORMAT STRING***
cool feature!

  
#lets say we got a variable:
vari="stuff"

we wanna print:
this variable contains stuff

$print(f"this variable contains {vari}")
this variable contains stuff

1-add f before the string to make format string
2-put variabe in {}

you can have functions and even other stuff here too

def cat():
    return "niaaa"
print(f"wow look {1+2*3**4} cats said {cat()})


"""

"""
***string manipulation and methods***

=> str.strip()  #removes whitespace(spac from left or right)

name="   h   "
print(name.strip())
h

=> str.capitalize() #capitilizes the FIRST LETTER 

name="abcd"
print(name.capitalize())
Abcd

=> str.title()  #capitalizes the first letter of each word

name="parsa soleimani"
print(name.title())
Parsa Soleimani


#YOU CAN DO str.strip().title.()
#thats nice

***split***
#i love this one

=> str.split() #splits the string by the string given

stri="a b c d"
print(stri.split())
['a', 'b', 'c', 'd']

a,b,c,d=stri.split("@")
#4 variables defined

stri="a@b@c@d"
print(stri.split("@"))
['a', 'b', 'c', 'd']
#this is cool



"""


"""

***int***

+   plus
-   negative
/   divide
%   remainder   
*   multiply
**  power

"""

"""

***float***

#like 1.23 or 4.56

=> float(thing) #turns it into a floating point

=> round(number[, ndigits]) #gives the nearest number with optional number of decimals

print(round(1.23456, 4))
1.2346


#f-string stuff

>>> z=1.222+2.333
>>> print(f"{z}")
3.555
>>> print(f"{z:,}")     #this will make numbers more readable
3.555
>>> print(f"{z:.2f}")   #this will only show two digits by rounding up
3.56

"""

"""

***functions/def***

def name _of_the_function([*arguments]):
    code
    return [*parameters]

>>> def street(name,vehicle,number):
...     print(f"{number} {vehicle} crossed the {name} street.")
... 

>>> street("street","car",6)
6 car crossed the street street.

***defaut value***

#to give a default value just put = and the default value after variable

>>> def street(name=goli,vehicle=tram,number=10):
...     print(f"{number} {vehicle} crossed the {name} street.")
... 

>>> street()
10 tram crossed the goli street.

#you can return stuff to

def sum(a,b):
    return a+b
print(sum(1,2))

***scope***

variables can be global or only in a function

"""
