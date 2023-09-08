

from datetime import date
import inflect
import sys

def main():
    rent=Rent(input("Date of Birth: "))
    print(f"{rent.correct_words()} minutes")
    
class Rent:
    def __init__(self,bdate):
        self.bdate=bdate
        self.cdate=date.today()

    @property
    def bdate(self):
        return self._bdate
    
    @bdate.setter
    def bdate(self,bdate):
        try:
            if len(bdate)==10:
                l=bdate.split("-")
                for i in range(len(l)):
                    l[i]=int(l[i])
                self._bdate=date(l[0],l[1],l[2])
            else:
                sys.exit(1)
        except:
            sys.exit(1)
    def num_to_word(self):
        return inflect.engine().number_to_words\
        ((self.cdate-self.bdate).days*24*60)
    
    def correct_words(self):
        cwords=self.num_to_word().capitalize().split("and ")
        owords=""
        for i in cwords:
            owords=owords+i
        return owords
        
def plusy(n1,n2):
    return n1+n2

if __name__ == "__main__":
    main()
