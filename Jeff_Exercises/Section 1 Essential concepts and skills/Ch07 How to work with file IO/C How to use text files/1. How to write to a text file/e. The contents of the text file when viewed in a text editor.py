# Ch07 How to work with file I/O
#  An introduction to file Input Output
#   How to use text files
#  The contents of the text file when viewed in a text editor 207
# Murach's Python programming 2 edition

# Web file I/O examples
# https://www.pythontutorial.net/python-basics/python-read-text-file/

# Title
# Code for Bold face text
start = "\033[1m"
end = "\033[0;0m"
print(start + '\nCh07 How to work with file IO' + end)
print(start + 'How to write to a text file' + end)
print('-' * 60)
print(start + "The contents of the text file when viewed in a text editor" + end)

# header
sp1 = (' ' * 5)
sp2 = (' ' * 8)
sp3 = (' ' * 22)
sp4 = (' ' * 25)
sp5 = (' ' * 35)
sp6 = (' ' * 7)
sp7 = (' ' * 13)
# Section 1
# Print table

print(sp1 + 'John Cleese' + '\n' + sp1 + 'Eric Idle' + '\n')
