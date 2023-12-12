# Ch06 How to work with lists and tuples
# How to work with tuples
#  A function that returns a tuple Page 195
# Murach's Python programming 2 edition

# Code for Bold face text
start = "\033[1m"
end = "\033[0;0m"
print(start + "\nMurach's Python programming 2 edition" + end)
print(start + '\nHow to work with tuples' + end)
print(start + ' A function that returns a tuple' + end)
print('-' * 60)

# # elements of section
sp1 = (' ' * 4)
sp2 = (' ' * 8)  # 8 spaces
sp3 = (' ' * 27)  # 26 spaces
sp4 = (' ' * 33)  # 30 spaces
sp5 = (' ' * 18)

print('def get_location():')
print(sp1 + 'return x, y, z')

print('\n' + start + 'Code that calls the get_location function and unpacks the returned tuple' + end)
print('x, y, z = get_location()')


def get_location():
    return x, y, z


x, y, z = get_location()
