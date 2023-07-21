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

# the string can be have and extra space or a , after it

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

tou can have functions and even other stuff here too

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



