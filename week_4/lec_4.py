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


*** statistics library ***

a library for some statistical work
like mean, median, mode etc

mean = average
median = the middle one
mode = the most occuring one

#a code using linear_regression

import random
import statistics
l_x=[1]
for i in range(20):
    l_x.append(l_x[-1]+random.randint(1,3))
l_y=[1]
for i in range(20):
    l_y.append(l_y[-1]+random.randint(1,3))

print(l_x)
print(l_y)
slope,intercept=statistics.linear_regression(l_x,l_y)
print(slope,intercept)
print()
print(statistics.mean(l_x))
print(statistics.median(l_x))
print(statistics.mode(l_x))



*** command line arguments ***
VERY IMPORTANT

--> sys

a module for interacting with the system

--> sys.argv()
# gets a vector(list) at the command line while executing
# ATTENTION: the argv[0] is the name of the file

import sys
try:    #if the user doesnt enter its their name
    name=sys.argv[1]
except:
    print("please enter your name at the end of the execution command")
else:
    print(f"your name is {name}")

-->sys.exit()

print something and exit the program

import sys
if len(sys.argv)<2 or len(sys.argv)>2:
    sys.exit("too many or few arguments")
print(f"your name is {sys.argv[1]}")

#this works the same

*** slices ***
#take a subset of a list

[a:b]   #starting from a to b (with a without b)
[a:]    #starting from a to end (with a)
[:b]    #starting from first to b (without b)

*** packages ***

pip3 install [package]

*** API/requests package ***

### requests
# a package that helps you work with APIs

--> requests.get()
#will get the response from a server
# an api for songs https://itunes.apple.com/search?entity=song&limit=1&term=weezer
# to work with the result(json) you should .json() at the end 

response=requests.get("api").json()

### json library
#allows to work with json better

-> json.dumps(response)
#prints the json file prettier

import json
import requests
response=requests.get(f"https://itunes.apple.com/search?entity=song&limit=1&term={input('artist= ')}").json()
print(json.dumps(response,indent=4))


import cowsay
import json
from pycoingecko import CoinGeckoAPI
cg=CoinGeckoAPI()
#print(cg.get_coin_ohlc_by_id(id="bitcoin", vs_currency="usd", days="14"))

import requests
response=requests.get(f"https://itunes.apple.com/search?entity=song&limit=10&term={input('artist= ')}").json()
for i in response["results"]:
    if i["artistName"]=="Yanni":
        print(i["trackName"])

# https://itunes.apple.com/search?entity=song&limit=1&term=drake


**** __name__ ***

it is a variable that when the file is directly called has the value of __main__

the reason for this:

if __name__==__main__:
    main()

is to only execute main() if the file is directly executed
it makes it easy to work with other files as library
"""