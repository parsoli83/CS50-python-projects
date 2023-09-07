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


# dont touch varibale that start with _ or __ :) 

*** @classmethod ***
#a decorator for a function related to the class not the object


class Transit:
    transit_modes={
        "metro":{"cap":"high"},
        "tram":{"cap":"medium"},
        "bus":{"cap":"low"},
        "LRT":{"cap":"medium/high"}
    }
    #this is a global variable
    def __init__(self,mode):
        self.mode =mode

    @property
    def mode(self):
        return self._mode
    
    @mode.setter
    def mode(self,mode):
        if mode in self.transit_modes:
            self._mode=mode
        else:
            raise ValueError
    
    def capacity(self):
        return self.transit_modes[self.mode]["cap"]
 
transit=Transit(input())
print(transit.capacity())


#you also can make a @classmethod
#for getting the data

class Transit:
    transit_modes={
        "metro":{"cap":"high"},
        "tram":{"cap":"medium"},
        "bus":{"cap":"low"},
        "LRT":{"cap":"medium/high"}
    }
    #this is a global variable
    def __init__(self,mode):
        self.mode =mode

    @classmethod
    def get(cls):
        mode=input()
        return cls(mode)

    @property
    def mode(self):
        return self._mode
    
    @mode.setter
    def mode(self,mode):
        if mode in self.transit_modes:
            self._mode=mode
        else:
            raise ValueError
    
    def capacity(self):
        return self.transit_modes[self.mode]["cap"]
 
transit=Transit(input())
print(transit.capacity())


--> classmethod
# a variable for the class that all objects can access

class Parsa:
    greetings=[
        "hi",
        "hello",
        "nice to meet you",
        "heyyy"
    ]
    @classmethod
    def say_hi(cls):
        print(random.choice(cls.greetings))

Parsa.say_hi()

*** inheritance ***
#when a class is subset of another
#it inherits its methods

class Transit:
    def __init__(self,mode,route):
        self.mode=mode
        self.route=route
        self.goodness="good"
    def is_good(self):
        return f"yes {self.mode},{self.route} is very good"
        

class LRT(Transit):
    def __init__(self,route,cap):
        super().__init__("LRT",route)
        self.cap=cap
    def capacity(self):
        return self.cap

lrt=LRT("AB","high")
print(lrt.is_good())
print(lrt.capacity())


operator overload is possible too


"""
