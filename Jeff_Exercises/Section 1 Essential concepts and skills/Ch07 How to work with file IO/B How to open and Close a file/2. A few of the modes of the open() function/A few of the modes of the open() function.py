# Ch07 How to work with file IO
#  An introduction to file Input Output
#   How to open and Close a file
#  A few of the modes of the open() function Page 205
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
print(start + "\nA few of the modes of the open() function" + end)

# header
sp1 = (' ' * 15)
sp2 = (' ' * 8)
sp3 = (' ' * 43)
sp4 = (' ' * 11)
sp5 = (' ' * 10)
sp6 = (' ' * 7)
sp7 = (' ' * 13)
# Section 1
# Print header
print('Character' + sp2 + 'Mode' + sp4 + 'Description')
print('-' * 60)

print(sp6 + 'r' + sp1 + 'Read' + sp4 + "If the file doesn't exist, this mode causes a file not found error.")
print(sp6 + 'w' + sp7 + 'Write' + sp7 + "If the file doesn't exist, this mode creates it. If the file already")
print(sp3 + 'exists, this module erases all existing data.')
print(sp6 + 'a' + sp7 + 'Append' + sp2 + "If the file doesn't exist, this mode creates it. If the file already")
print(sp3 + 'exists, this mode appends the data to the end of the file.')
print(sp6 + 'b' + sp7 + 'Binary' + sp5 + "Use for binary files along with 'r' or 'w' mode.")
