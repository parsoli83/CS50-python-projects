def main():
    price=50
    paid=0
    while True:
        print("Amount Due:",price-paid)
        paid+=valid_coin(price-paid)
        if price-paid<=0:
            print("Change Owed:",paid-price)
            break

def valid_coin(amount_due):
    while True:
        inp=int(input("Insert Coin: "))
        if inp==5 or inp==10 or inp==25:
            return inp
        
        print("Amount Due:",amount_due)



main()