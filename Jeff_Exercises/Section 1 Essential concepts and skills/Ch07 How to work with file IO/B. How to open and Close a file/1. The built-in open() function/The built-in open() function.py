# Ch07 How to work with file IO
#  An introduction to file Input Output
#   How to open and Close a file
#  The built-in open() function, Page 205
# Murach's Python programming 2 edition

# Web file I/O examples
# https://www.pythontutorial.net/python-basics/python-read-text-file/

# Title
# Code for Bold face text
start = "\033[1m"
end = "\033[0;0m"
print(start + '\nCh07 How to work with file IO' + end)
print(start + 'How to open and Close a file ' + end)
print(start + "\nThe built-in open() function" + end)

# header
sp1 = (' '*15)
sp2 = (' '*7)
print('-'*60)

# Section 1
from tabulate import tabulate

# assign data
openFileData = [
    ['Open(file, mode)', 'Returns a file object for the specified file with the spectified mode']
]

# create header
headFileData = ['Function' + (' '*15), (' '*5)  + 'Description']

# display table
print(tabulate(openFileData, headers=headFileData, tablefmt='fancy'))

