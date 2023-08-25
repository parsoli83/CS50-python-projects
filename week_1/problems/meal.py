#inp=input("What time is it? ").split()
def main():
    time=convert(input("What time is it? "))
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")
    else:
        print()


def convert(time):
    inp=time.split()
    t=inp[0].split(":")
    h=int(t[0])
    m=int(t[1])
    if len(inp)==2:
        if inp[1]=="p.m.":
            h=h+12
    return h+m/60



if __name__ == "__main__":
    main()

