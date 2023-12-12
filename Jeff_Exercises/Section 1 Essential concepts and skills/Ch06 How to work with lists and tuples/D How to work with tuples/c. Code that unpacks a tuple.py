# Ch06 How to work with lists and tuples
# How to work with tuples
#  Code that unpacks a tuple, Page 195
# Murach's Python programming 2 edition

# Code for Bold face text
start = "\033[1m"
end = "\033[0;0m"
print(start + "\nMurach's Python programming 2 edition" + end)
print(start + '\nHow to work with tuples' + end)
print(start + ' Code that unpacks a tuple' + end)
print('-' * 60)

# # elements of section
sp1 = (' ' * 4)
sp2 = (' ' * 8)  # 8 spaces
sp3 = (' ' * 27)  # 26 spaces
sp4 = (' ' * 33)  # 30 spaces
sp5 = (' ' * 18)

print('tuple_values = (1, 2, 3)')
tuple_values = (1, 2, 3)
a, b, c = tuple_values  # a = 1, b = 2, c = 3
print('a, b, c = tuple_values         # a = 1, b = 2, c = 3')
print('Print the values: ')
print('a = ', a)
print('b = ', b)
print('c = ', c)
