# Ch06 How to work with lists and tuples
# How to copy, slice, and concatenate lists
#  How to slice a list, Page 189
# Murach's Python programming 2 edition

from numpy.core.defchararray import lower

# Code for Bold face text
start = "\033[1m"
end = "\033[0;0m"
print(start + '\nCh06 Basic skills for working with lists' + end)
print(start + 'More skills for working with lists' + end)
print(start + ' How to slice a list' + end)
print('-' * 60)

# # elements of section
sp1 = (' ' * 4)
sp2 = (' ' * 8)  # 8 spaces
sp3 = (' ' * 14)  # 26 spaces
sp4 = (' ' * 17)  # 30 spaces
sp5 = (' ' * 35)
sp6 = (' ' * 39)
print()

# Code that slices with the start and end arguments'
print('-' * 60)
print(start + 'The syntax for slicing a list' + end)
print('mylist = [start:end:step]')
print(start + 'Code that slices with the start and end arguments' + end)
print('numbers = [52, 54, 56, 58, 60, 62]')
print('numbers[0:2]          # [52, 54]')
print('numbers[:2]            #  [52, 54]')
print('numbers[4:]            # [60, 62]')

print('\nCode:')
numbers = [52, 54, 56, 58, 60, 62]
print('numbers[0:2] is: ', numbers[0:2])
print('numbers[:2] is: ', numbers[:2])
print('numbers[4:] is: ', numbers[4:])

# Code that slices with the step argument

print('numbers = [52, 54, 56, 58, 60, 62]')
print('numbers[0:4:2]          # [52, 56]')
print('numbers[::-1]            #  [62, 60, 58, 56, 54, 52]')

print('\nCode:')
numbers = [52, 54, 56, 58, 60, 62]
print('numbers[0:4:2]  is: ', numbers[0:4:2])
print('numbers[::-1] is: ', numbers[::-1])
