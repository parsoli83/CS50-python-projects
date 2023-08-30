from random import randint
def main():
    n=randint(1,get_input("Level: "))
    while True:
        guess=get_input("Guess: ")
        if guess>n:
            print("Too large!")
        elif guess==n:
            print("Just right!")
            break
        else:
            print("Too small!")

def get_input(message):
    while True:
        try:
            n=int(input(message))
            if n>0:
                return n
        except:
            continue
        else:
            continue
        



if __name__=="__main__":
    main()