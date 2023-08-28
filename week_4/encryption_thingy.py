import random
import string
ascii_letters=string.ascii_letters

def main():
    original=input("text: ")
    print(f"{starter()}{parasiter(original)}{ender()}")


def starter():
    phrase=""
    for i in range(random.randint(1,6)):
        phrase+=random.choice(ascii_letters)
    return f"{phrase}<"

def ender():
    phrase=">"
    for i in range(random.randint(1,6)):
        phrase+=random.choice(ascii_letters)
    return phrase

def parasiter(text):
    cypher=""
    for i in text:
        cypher+=i
        local_key=random.randint(0,6)
        if random.randint(0,6)==0:
            shit=underline_adder()
            if shit!=None:
                cypher=f"{cypher}{shit}"
    return cypher
def underline_adder():
    return "_"*two_based_log()

def two_based_log(times=1):
    if random.randint(0,1)==0:
        return times
    return two_based_log(times+1)

main()