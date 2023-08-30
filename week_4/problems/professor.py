import random


def main():
    solved=0
    level=get_level()
    for i in range(10):
        if trial(generate_integer(level),generate_integer(level)):
            solved+=1
    print(f"Score: {solved}")
    

        


def get_level():
    while True:
        try:
            level=int(input("Level: "))
            if 1<=level<=3:
                return level
            else:
                continue
        except EOFError:
            raise EOFError
        except ValueError:
            continue

def generate_integer(level):
    if not 1<=level<=3:
        raise ValueError
    else:
        if level==1:          
            return random.randint(0,10**level-1)
        else:
            return random.randint(10**(level-1),10**level-1)


def trial(n1,n2):
    for i in range(3):
        try:
            user_answer=int(input(f"{n1} + {n2} = "))
            if user_answer==n1+n2:
                return True
            else:
                print("EEE")
                continue
        except EOFError:
            raise EOFError       
        except:
            print("EEE")
            continue
    print(f"{n1} + {n2} = {n1+n2}")
    return False



if __name__ == "__main__":
    main()
