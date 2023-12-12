# Ch07 How to work with file IO
#  An introduction to file Input Output
#  How to use binary files
#  How to work with a binary file
# How to write an object to a binary file Page 225
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
print(start + "How to write an object to a binary file" + end)

# header
sp1 = (' ' * 5)
sp2 = (' ' * 8)
sp3 = (' ' * 22)
sp4 = (' ' * 35)
sp5 = (' ' * 20)
sp6 = (' ' * 32)
sp7 = (' ' * 13)

print(sp1 + 'with open("movies.bin", "rb") as file:' + sp3 + '# use rb mode for read binary')
print(sp2 + 'pickle.dump(movies, file)')

print('\nCode:')
import pickle
