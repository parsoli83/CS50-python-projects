"""
### errors ###

*** SyntaxError ***

an error caused by what you typed that broke the syntax

*** ValueError ***

when an invalid value is given to a function

*** runtime error ***

errors that occure during runtime

*** NameError ***

when a variable or anything is not defined but used

### error handling ###

*** try/except ***

# lets give an example

try:    #tries the following code
    print(int(input()))
except: #does this if things go wrong
    print("give a number")

# except can be implemented this way too

try:
    print(int(input()))
except ValueError:  #just for ValueError
    print("give a number")

*** else ***

what you do when nothing else is relevant

take this as an example

try:
    print(int(input()))
    x=2
except:
    print("give a number")
print(x)

#and you input g
#since the error occures before the x=2 theres no x
#therefore you get an error in print(x)

#else is used when things in try go well

try:
    print(int(input()))
    x=2
except:
    print("give a number")
else:
    print(x)

# you can use break at the end of try in loops

#ATTENTION

a try has a global scope
and variables defined BEFORE THE ERROR are there

try:
    x=2
    print(int(input()))
except:
    print("give a number")
print(x)

this is gonna give you(upon entering a letter like g)

g
give a number
2

*** pass ***

when you catch an error but you dont wanna do anything with it

try:
    x=2
    print(int(input()))
except:
    pass
print(x)

try:
    x=2
    print(int(input()))
except ValueError:
    print("give a number")
except SyntaxError:
    print("syntax")
except NameError:
    print("nameerror")
except:
    pass
else:
    print("ok")


"""
