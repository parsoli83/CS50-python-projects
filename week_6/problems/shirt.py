from PIL import Image,ImageOps
import sys
def main():
    generate(get_input())
def get_input():
    l_formats=["png","jpg","jpeg"]
    arguments=sys.argv
    if len(arguments)<3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(arguments)>3:
        print("Too many command-line arguments")
        sys.exit(1)
    else:
        if arguments[1].split(".")[-1] not in l_formats:
            print("Invalid input")
            sys.exit(1)
        elif arguments[1].split(".")[-1]!=arguments[2].split(".")[-1]:
            print("Input and output have different extensions")
            sys.exit(1)
        else:
            return arguments
        
def generate(arguments):
    before=arguments[1]
    after=arguments[2]
    with Image.open(before) as img:
        with Image.open("shirt.png") as shirt:
            size=shirt.size
            new_img = ImageOps.fit(img, size)
            new_img.paste(shirt,shirt)
            new_img.save(after)





if __name__=="__main__":
    main()