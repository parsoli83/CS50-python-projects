
def main():
    l_names=get_input()
    if len(l_names)==1:
        print(f"Adieu, adieu, to {l_names[0]}")
    elif len(l_names)==2:
        print(f"Adieu, adieu, to {l_names[0]} and {l_names[1]}")
    else:
        print(f"Adieu, adieu, to {comma_generator(l_names[:-1])}and {l_names[-1]}")



def get_input():
    l_names=[]
    while True:
        try:
            l_names.append(input("Name: "))
        except EOFError:
            print()
            return l_names
def comma_generator(l_names):
    comma_names=""
    for name in l_names:
        comma_names+=f"{name}, "
    return comma_names



if __name__=="__main__":
    main()