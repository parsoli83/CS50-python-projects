def main():
    grocery_dic={}
    while True:
        item=get_input()
        if item==0:
            number_printer(grocery_dic)
            return 0
        else:
            if item in grocery_dic:
                grocery_dic[item]=grocery_dic[item]+1
            else:
                grocery_dic[item]=1
        
def get_input():
    try:
        return input().upper()
    except EOFError:
        return 0

def number_printer(grocery_dic):
    items=list(grocery_dic.keys())
    items=sorted(items)
    for i in items:
        print(f"{grocery_dic[i]} {i}")

main()