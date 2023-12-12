# Ch07 How to work with file IO
#  An introduction to file Input Output
#   How to open and Close a file
#  The close() method of a file objectPage 205
# Murach's Python programming 2 edition

# Web file I/O examples
# https://www.pythontutorial.net/python-basics/python-read-text-file/

# Title
# Code for Bold face text
start = "\033[1m"
end = "\033[0;0m"
print(start + '\nCh07 How to work with file IO' + end)
print(start + 'How to open and Close a file ' + end)
print()
print('-' * 60)
print(start + "\nThe close() method of a file object\n" + end)

# header
sp1 = (' ' * 4)
sp2 = (' ' * 8)
sp3 = (' ' * 43)
sp4 = (' ' * 11)
sp5 = (' ' * 10)
sp6 = (' ' * 7)
sp7 = (' ' * 13)
# Section 1
# Print header
print('Method' + sp2 + 'Description')
print('-' * 60)

print('close( )' + sp2 + "Closes the file, which ends all operations and frees all resources.")
