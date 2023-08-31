from curses.ascii import isalpha


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    def fourth_law(s):
        l=[" ",",","!","."]
        for i in s:
            if i in l:
                return False
        return True

    def first_law(s):
        if s[0].isalpha() and s[1].isalpha():
            return True
        return False

    def third_law(s):
        key=0
        # 0 for letter till now
        # 1 for number seen
        for i in range(len(s)):
            if not s[i].isalpha():  #is number
                if key==0:
                    if s[i]=="0":
                        return False
                    key=1
            else:   #is letter
                if key==1:
                    return False
        return True
    if 2<=len(s)<=6:
        if fourth_law(s):
            if first_law(s):
                if third_law(s):
                    return  True
    return False

if __name__ == "__main__":
    main()