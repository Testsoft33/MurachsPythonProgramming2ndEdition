# Ch06 How to work with lists and tuples
# Basic skills for working with lists
# How to get an item in a list, Page 165
# Murach's Python programming 2 edition

# Title
# Code for Bold face text
start = "\033[1m"
end = "\033[0;0m"
print(start + '\nCh06 How to work with lists and tuples' + end)
print(start + 'Basic skills for working with lists' + end)
print('-' * 60)
print(start + "How to get an item in a list" + end)
print(start + "   Code that gets items from the temps list" + end)

# section 1
# elements of section
sp1 = (' ' * 10)

string1 = '   temps = [48.0, 30.5, 20.2 100.0, 42.0]'
string2 = '   temp = temps[0]'
string3 = '# temp = 48.0'
string4 = '   temp = temps[4]'
string5 = '# temp = 42.0'
string6 = '   temp = temps[5]'
string7 = '# IndexError: index out of range'

# Print strings
print('{}\n{}{}{}\n{}{}{}\n{}{}{}'
      .format(string1, string2, sp1, string3, string4, sp1, string5, string6, sp1, string7))

# section 2
# elements of section
sp1 = (' ' * 10)
print(start + "\n   Code that gets items from the inventory list" + end)
string1 = '   inventory = ["staff", "hat", "shoes", "bread", "potion", "scroll1"]'
string2 = '   item = inventory[5]'
string3 = '# item = "scroll"'
string4 = '   item = inventory[3]'
string5 = '# item = "bread"'
string6 = '   item = inventory[6]'
string7 = '# IndexError: index out of range'

# Print strings
print('{}\n{}{}{}\n{}{}{}\n{}{}{}'
      .format(string1, string2, sp1, string3, string4, sp1, string5, string6, sp1, string7))
