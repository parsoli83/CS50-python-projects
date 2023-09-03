import sys

def main():

    arguments=sys.argv
    if len(arguments)<2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(arguments)>2:
        print("Too many command-line arguments")
        sys.exit(1)
    else:
        if arguments[1].split(".")[-1]!="py":
            print("Not a Python file")
            sys.exit(1)
        else:
            try:
                with open(arguments[1],"r") as file:
                    line_counter(file)
            except FileNotFoundError:
                print("File does not exist")
                sys.exit(1)
        
        
def line_counter(file):
    text=file.read().split("\n")
    total=0
    for line in text:
        line=line.strip()
        if line=="":
            continue
        elif line[0]=="#":
            continue
        else:
            total+=1
    print(total)

if __name__=="__main__":
    main()
