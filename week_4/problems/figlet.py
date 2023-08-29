from random import choice
from pyfiglet import Figlet
from sys import exit,argv
def main():
    figlet=Figlet()
    global l_fonts
    l_fonts=figlet.getFonts()

    l=get_input()
    if len(l)==1:
        figlet.setFont(font=l_fonts.choice())
    else:
        figlet.setFont(font=l[1])
    print("Output: ")
    print(figlet.renderText(l[0]))

def get_input():

        l_inp=argv
        if len(l_inp)==3:
            if l_inp[1]=="-f" or l_inp[1]=="--font":
                if l_inp[2] in l_fonts:
                    return [input("Input: "),l_inp[2]]
                else:
                    exit("Invalid usage")
            else:
                exit("Invalid usage")
        elif len(l_inp)==1:
            return [input("Input: ")]       
        else:
            exit("Invalid usage")
        

if __name__=="__main__":
    main()