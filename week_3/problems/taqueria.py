menu_dict={
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
def main():
    total=0
    while True:
        food_price=get_input()
        if food_price==0:
            return 0
        total+=food_price
        print(f"Total: ${total:.2f}")

def get_input():
    while True:
        try:
            food_name=input("Item: ").lower().title()
            return menu_dict[food_name]
        except EOFError:
            print()
            return 0
        except:
            continue

    


main()