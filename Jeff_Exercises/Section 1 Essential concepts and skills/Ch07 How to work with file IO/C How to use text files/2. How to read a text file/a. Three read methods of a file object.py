# Ch07 How to work with file IO
#  An introduction to file Input Output
#   How to use text files
#  Three read methods of a file object page 209
# Murach's Python programming 2 edition

# Web file I/O examples
# https://www.pythontutorial.net/python-basics/python-read-text-file/

# Title
# Code for Bold face text
start = "\033[1m"
end = "\033[0;0m"
print(start + '\nCh07 How to work with file IO' + end)
print(start + 'How to read a text file' + end)
print('-' * 60)
print(start + "Three read methods of a file object" + end)

# header
sp1 = (' ' * 5)
sp2 = (' ' * 8)
sp3 = (' ' * 27)
sp4 = (' ' * 29)
sp5 = (' ' * 24)
sp6 = (' ' * 22)
sp7 = (' ' * 13)
# Section 1
# Print table

print('\nMethod' + sp3 + 'Descriptions')
print('-' * 60)
print('read()' + sp4 + 'Reads the entire file and returns its contents as a string.')
print('readlines()' + sp6 + 'Reads the entire  file and returns it as a list.')
print('readline()' + sp5 + 'Reads the next line in the  file and returns its contents as a string.')
