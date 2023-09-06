from validator_collection import is_email




def main():
    print(validator(input("What's your email address? ")))


def validator(s):
    if is_email(s):
        return "Valid"
    return "Invalid"


if __name__ == "__main__":
    main()