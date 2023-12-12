# Ch06 How to work with lists and tuples
# Basic skills for working with lists
# The syntax for creating a list, Page 165
# Murach's Python programming 2 edition

# Title
# Code for Bold face text
start = "\033[1m"
end = "\033[0;0m"
print(start + '\nCh06 How to work with lists and tuples' + end)
print(start + 'Basic skills for working with lists' + end)
print('-' * 60)
print(start + "The syntax for creating a list" + end)

# section 1
string1 = 'list_name = [item1, item2, ...]'

# Print strings
print('   {}'.format(string1, ))

# section 2
# Title of section
string1 = (start + 'Code that creates lists' + end)
# elements of section
sp1 = (' ' * 10)
sp2 = (' ' * 12)
sp3 = (' ' * 10)
sp4 = (' ' * 32)
string2 = 'temps = [48.0, 30.5, 20.2, 100.0, 42.0'
string3 = '# 5 float values'
string4 = 'inventory = ["staff", "hat", "shoes"'
string5 = '# str values'
string6 = 'movie = ["The Holy Grail", 1975, 9.99]'
string7 = '# str, int, and float values'
string8 = 'test_scores = []'
string9 = '# an empty list'
# Print strings
print('\n   {}\n   {}{}{}\n   {}{}{}\n   {}{}{}\n   {}{}{}'
      .format(string1, string2, sp1, string3, string4, sp2, string5,
              string6, sp3, string7, strin8, sp4, string9))
