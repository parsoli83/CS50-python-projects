"""
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

"""
def main():
    print(gauge(convert(input("Fraction: "))))


def convert(fraction):
    try:
        inp=fraction.split("/")
        percentagee=int(inp[0])/int(inp[1])
        if percentagee<=1 and percentagee>=0:
            return round(percentagee*100)
    except ZeroDivisionError:
        raise ZeroDivisionError
    except ValueError:
        raise ValueError
        


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
