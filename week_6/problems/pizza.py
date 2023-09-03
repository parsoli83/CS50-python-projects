import sys
from tabulate import tabulate
import csv

def get_input():

    arguments=sys.argv
    if len(arguments)<2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(arguments)>2:
        print("Too many command-line arguments")
        sys.exit(1)
    else:
        if arguments[1].split(".")[-1]!="csv":
            print("Not a CSV file")
            sys.exit(1)
        else:
            try:
                with open(arguments[1],"r") as file:
                    return ascii_csv(file)
            except FileNotFoundError:
                print("File does not exist")
                sys.exit(1)
        

def main():
    print(get_input())

def ascii_csv(file):
    csv_file=csv.reader(file)
    table=list(csv_file)
    return tabulate(table[1:],table[0],tablefmt="grid")

if __name__=="__main__":
    main()
