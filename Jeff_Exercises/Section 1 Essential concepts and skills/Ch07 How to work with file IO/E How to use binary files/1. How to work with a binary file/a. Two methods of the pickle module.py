# Ch07 How to work with file IO
#  An introduction to file Input Output
#  How to use binary files
#  How to work with a binary file
#   Two methods of the pickle module Page 225
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
print(start + "Two methods of the pickle module" + end)

# header
sp1 = (' ' * 5)
sp2 = (' ' * 8)
sp3 = (' ' * 18)
sp4 = (' ' * 35)
sp5 = (' ' * 20)
sp6 = (' ' * 32)
sp7 = (' ' * 13)

print('\nMethod' + sp4 + 'Description')
print('-' * 70)
print('dump(object, bfile)' + sp3 + 'Writes the specified object to the specified file.')
print('load(bfile)' + sp6 + 'Reads an object from the specified binary file.')
