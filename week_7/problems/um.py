
import re


def main():
    print(count(input("Text: ")))


def count(s):
    s=s.strip()
    middle= len(re.findall(r"[^a-z]um[^a-z]",s, re.IGNORECASE))
    start= len(re.findall(r"^um[^a-z]",s, re.IGNORECASE))
    end= len(re.findall(r"[^a-z]um$",s, re.IGNORECASE))
    meow= len(re.findall(r"^um$",s, re.IGNORECASE))
    return middle + start + end + meow


if __name__ == "__main__":
    main()
