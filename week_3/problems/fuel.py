def main():
    percentage=get_input()
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")

def get_input():
    while True:
        try:
            inp=input("Fraction: ").split("/")
            percentagee=int(inp[0])/int(inp[1])
            if percentagee<=1 and percentagee>=0:
                return round(percentagee*100)
        except:
            continue
main()