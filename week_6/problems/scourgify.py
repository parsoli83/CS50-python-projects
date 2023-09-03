import sys
import csv

def main():
    get_input()




def get_input():
    arguments=sys.argv
    if len(arguments)<3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(arguments)>3:
        print("Too many command-line arguments")
        sys.exit(1)
    else:
        if arguments[1].split(".")[-1]!="csv" or \
        arguments[2].split(".")[-1]!="csv":
            print("Not a CSV file")
            sys.exit(1)
        else:
            try:
                with open(arguments[1],"r") as file:
                    return after_maker(file,arguments[2])
            except FileNotFoundError:
                print(f"Could not read {arguments[1]}")
                sys.exit(1)


def after_maker(file,name):
    before_reader=list(csv.reader(file))
    with open(name,"w") as after:
        after.write("first,last,house\n")
    
    for i in range(1,len(before_reader)):
        line=before_reader[i][0].split(",")
        first=line[0].strip()
        last=line[1].strip()
        
        with open(name,"a") as after:
            after.write(f"{last},{first},{before_reader[i][1]}\n")
      


if __name__=="__main__":
    main()