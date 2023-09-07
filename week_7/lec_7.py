"""
*** Regex ***
# the game of patterns :)
import re

-->re.search(pattern,string,flags=)
#returns a boolian of whether the pattern
#exists in string

re.match()  start from the beginning
re.fullmatch()    start and end by this

re.sub(pattern,replace_with_what,string)
# basically a replacing method


# the pattern can be configured
*** re symbols ***

.   any character except \n
*   0 or more repetitions
+   1 or more repetitions
?   0 or 1 repetition
{m}    m repetitions
{m,n}   m-n repetitions

# placement:

^   start with
$   end with(before the new-line at end)

# set of characters

[]    things you want
[^]    things you dont want

#[abc] means only a or b or c
#[^a^b] means anything BUT a or b

# for having a set of characters:

[a-z]    a to z lowecase
[A-Z]    A to Z uppercase
[0-9]    aloow 0 to 9

[a-zA-Z0-9_]    
#accept everything a-z and A-Z and 0-9 and _
which also can be represtented as :
### \w ###
alpha-numerical plus underscore 


A|B    a or b
(...)    a group
(?:...)    non-c apturing group

(com|net|gov)    one of these:)
(?:ir|ru)    not one of these:(

*** (...) for capturing ***

#() can be used for getting values from RE
# store the re.search in a variable
# variabe.groups() to get the values

import re
matches=re.search(r"(\w*)&(\w*)$","SD&ba")
if matches:
    a,b=matches.groups()

    #or
    #a=matches.group(1)
    #b=matches.group(2)    yes start from 1
    print(a,b)

*** := (walrus operator)***
# assign a value and check if true

import re
if matches := re.search(r"(\w*)&(\w*)$","SD&ba"):
    a,b=matches.groups()
    print(a,b)


*** re flags ***

re.IGNORECASE   ignore the case of user input

re.MULTILINE    when you wanna re a paragraph

eg:

re.search(".*@.*",email,re.IGNORECASE)



# how they behave:

".*@.*"    something(0-inf characters) at each end
".+@.+"    something(1-inf characters) at each end
".?@.?"    something(0-1 characters) at each end   
".{3}@.{3}"    something(3 characters) at each end
".{3,5}@.{3,5}"    something(3-5 characters) at each end

"^..*@..*"    should start with this
"..*@..*$"    should end with this
"^..*@..*$"    should start and end with this


"[abc]+@[abc]+"    1 or more of the characters a,b,c at each side
"[^@]+@[^@]+"    1 or more of anything but @ at each end  

# when you literally mean one of the keywords
# eg: i want .com at the end

### use \. or \? or \}
### put r before string to make raw string r""

r".+@.+\.com"    # as easy as that :)

 

### cool feature: you can check if variables exist

if variable
    # it exists
else
    # it doesnt exist

### str.endswith(str)

email="abc@gmail.com"
if str.endswith("@gmail.com"):
    print(True)

"""