"""

*** file I/O ***

--> open(file, mode='r', buffering=- 1, encoding=None,
 errors=None, newline=None, closefd=True, opener=None)


 ### different modes

# "w" : create and overwrite the file (truncate it)

# "a" : appends to the end of the file and creates it
# if it doesnt exist

# "r" : read only
# "r+" : read and write

--> file.write(what you wanna write)

--> file.close()

*** with ***
# it is a clean way of doing a sort of try/except/else/finally

#it is good practice since it automatically coses the file when things are done

#this code:

file = open('file-path', 'w') 
try: 
    file.write('Lorem ipsum') 
finally: 
    file.close() 

#is equal to this code

with open('file-path', 'w') as file: 
    file.write('Lorem ipsum') 

--> file.read()
#simply reads the file as text

-->file.readline()
# reads the file and return a list split by each line(\n)
# keep in mind items are returned with the \n

# a better practice would be:

file.read().split("\n")
# no \n in the returned items :)
# and you also can split() by anything

### COOL FEATURE : you can iterate in file by \n

def main():
    with open("some_text.txt","r") as file:
        for i in file:
            print(file.rstrip())    # this removes th \n

*** sorted ***

# you can tell the sorted() function to sort by what

get_name = lambda student : student["name"]
for student in sorted(students , key=get_name):
    print(student)

# now things are sorted by the name of the students

*** lambda ***

name = lambda parameter1, parameter2 = returned_thingy

*** csv ***

# comma seperated values :)

--> csv.reader(file)
with open("file.csv",r) as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # a list

--> csv.Dictreader(file)
# reads the csv as a dictionary

name,luck
user_0,18

{'nname': 'user_0', 'luck': '18'}

--> csv.writer(file)

with open("file.csv",r) as file:
    writer = csv.writer(file)
    writer.writerow([a, b])

--> csv.dictwriter(file, fieldnames=[a,b])
# fieldnames is given to keep the order

with open("file.csv",r) as file:
    writer = csv.writer(file)
    writer.writerow({"a":a,"b":b})


*** pillow ***
# a librrary for imgae/gif/video

from PIL import Image
import sys
import csv
def main():
    gif_creator(get_input())


def gif_creator(l_image_names):
    try:
        l_images=[]
        for name in l_image_names:
            l_images.append(Image.open(name))
    except:
        print("invalid image names")
    else:
        l_images[0].save(
            "the_gif.gif",save_all=True, \
            append_images=l_images[1:],\
            duration=1000,loop=0
        )




def get_input():
    try:
        return sys.argv[1:]
    except EOFError:
        raise EOFError
    except:
        print("give arguments")
    
        
        
if __name__=="__main__":
    main()

"""
