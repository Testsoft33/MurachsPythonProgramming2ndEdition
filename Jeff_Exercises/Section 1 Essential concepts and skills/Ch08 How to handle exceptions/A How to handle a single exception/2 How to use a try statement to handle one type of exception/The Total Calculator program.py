# The user interface

# The code
def get_price():
    while True:
        try:
            price = float(input("Enter price: "))
            return price
        except ValueError:
            print("Invalid decimal number. Please try again")

def get_quantity():
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            return quantity
        except ValueError:
            print("Invalid integer. Please try again.")

def main():
    print("The Total of Calculator program\n")

    # get the price and quantity
    price = get_price()
    quantity = get_quantity()

    # Calculate the total
    total = price * quantity

    # displays the results
    print()
    print("PRICE:     ", price)
    print("QUANTITY:  ", quantity)
    print("TOTAL:     ", total)

if  __name__ == "__main__":
    main()
