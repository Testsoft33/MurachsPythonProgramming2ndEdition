# Int Float And Round page 54 - 58  Chapter 2
# Murach's Python programming 2 edition'''

# int() function
x = 15
y = '5'
z = x +  int(y)
print('#1 is: ', z)
print()

# Code that gets int value from the user
quantity = input('Enter the quanity: ')     # quantity is string type
quantity = int(quantity)        # quantity is int type
print('#2 Quantity is: ', quantity)

# How to use chaining to get the int value in one statement
quantity = int(input('\nEnter the quantity: '))
print('#3 Quantity is now: ', quantity)


# Code that gets How to code if statements float value from the user
price = input('\nEnter the price: ')      # price is string type
price = float(price)        # price is float type
print('#4 Price is: ', price)

# How to use chaining to get the float value in one statement
price = float(input('\nEnter the price per gallon of gas: '))
print('#5 Price is: ', price)

# Code that uses the round() function
miles_driven = 150
gallons_used = 5.875
mpg = miles_driven / gallons_used
mpg = round(miles_driven / gallons_used, 2)
print('\n#6 mpg is: ', mpg)

# How to combine the last two statements
mpg = round(miles_driven / gallons_used, 2)
print('\nmpg is: ', mpg)