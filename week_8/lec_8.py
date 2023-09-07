"""

tuple:
use ()
list but immutative

 
*** OOP *** 

class:
# allows you to invent your own data type

object:
# an object of a class 
#(class is like a frame and object what cmes out of it)
class student:

# an example:

class shit:
    ...

poo=shit()
poo.color="brown"
poo.smell="bad"
poo.size="medium"

print(poo.size,poo.smell,poo.color)

pee=shit()
pee.color="yellow"
pee.state="liquid"

print(pee.color,pee.state)

--> instance-variable
# like poo.size or pee.color

--> attribute
# variables shared between all objects of a class

--> method
# a function inside a class

--> __init__

it is the function called
when initiallizing an object

def __init __(self,var1,var2):
    self.var1=var1
    self.var2=var2

# EG:

class shit:
    def __init__(self,state,color,smell):
        self.state=state
        self.color=color
        self.smell=smell

pee = shit("solid","brown","bad")
print(pee)

*** raise ***

raises an error
like:
raise ValueError  

class shit:
    def __init__(self,state,color,smell):
        if state not in ("solid","iquid"):
            raise ValueError("Invalid state")
        if not color:
            raise ValueError("no color given")
        self.state=state
        self.color=color
        self.smell=smell

--> __str__
when another thing wants to see your object as string

class shit:
    def __init__(self,state,color,smell):
        if state not in ("solid","iquid"):
            raise ValueError("Invalid state")
        if not color:
            raise ValueError("no color given")
        self.state=state
        self.color=color
        self.smell=smell
    def __str__(self):  #here it is!
        return "a piece of shit with these characteristics"

# you also can define methods(functions)

class shit:
    def __init__(self,state,color,smell):
        self.state=state
        self.color=color
        self.smell=smell
    def show_up(self):
        print(f"hello I'm {self.name} :)")

*** properties ***

some attributes that we have moe control on how it changes

--> decorators:
#functions that modify the behaviour of other functions

class shit:
    def __init__(self,state,color,smell):
        self.state=state
        self.color=color
        self.smell=smell

    # for getter 
    @property
    def smell(self):
        return self._smell  #pay attention to _
    
    # for setter
    @smell.setter
    def smell(self,smell):
        if smell not in ["bad","awful","toxic"]:
            raise ValueError
        else:
            self._smell=smell   #pay attention to _

### EXPLANATION:

1:  @property for getter
# is used to make a getter
# it gets the value
# remember to put _ before the variable name
# because it has the same name as function


2:  @{var_name}.setter for setter
# sets the value for the variable
# you can error check here
# remember to put _ before the variable name
# because it has the same name as function




"""


class shit:
    def __init__(self,state,color,smell):
        self.state=state
        self.color=color
        self.smell=smell 
    @property
    def smell(self):
        return self._smell
    
    @smell.setter
    def smell(self,smell):
        if smell not in ["bad","awful","toxic"]:
            raise ValueError
        else:
            self._smell=smell


pee=shit("solid","brown","bad")
pee.smell="good"
print(pee.smell)