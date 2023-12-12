# Ch07 How to work with file IO
#  An introduction to file Input Output
#  How to use binary files
#  How to work with a binary file
#   A two-dimensional list with 3 rows and 2 columns Page 225
# Murach's Python programming 2 edition

import csv

# Title
# Code for Bold face text
start = "\033[1m"
end = "\033[0;0m"
print(start + '\nCh07 How to work with file IO' + end)
print(start + 'How to use binary files' + end)
print(start + "How to work with a binary file" + end)
print('-' * 60)
print(start + "A two-dimensional list with 3 rows and 2 columns" + end)

# header
sp1 = (' ' * 5)
sp2 = (' ' * 8)
sp3 = (' ' * 22)
sp4 = (' ' * 35)
sp5 = (' ' * 20)
sp6 = (' ' * 32)
sp7 = (' ' * 13)

print(sp1 + 'movies =  [["Monty Python and the Holy Grail", 1975],')
print(sp3 + '["Cat on a Hot Tin Roof", 1958],')
print(sp3 + '["On the Waterfront", 1954] ]')
