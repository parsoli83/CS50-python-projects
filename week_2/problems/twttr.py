def main():
    wordi=input("Input: ")
    print("Output:",shortner(wordi))



def shortner(word):
    shrtd=""
    for i in word:
        if not_vow(i):
            shrtd=shrtd+i
    return shrtd

def not_vow(i):
    vow=["a","e","o","u","i"]
    voww=["A","E","O","U","I"]
    if i not in vow and i not in voww:
        return True
    return False


main()