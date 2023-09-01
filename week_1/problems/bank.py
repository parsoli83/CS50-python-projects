def main():
    print(value(input("Greeting: ").lower().strip()[:5]))


def value(greet):
    greeting=greet.lower()
    if greeting=="hello":
        return"$0"
    elif greeting[0]=="h":
        return"$20"
    return"$100"


if __name__ == "__main__":
    main()
