# Ch07 How to work with file IO
#  An introduction to file Input Output
#   How to use text files
# How to work with a list in a text file
#  How to write and read a list of strings page 211
# Murach's Python programming 2 edition

# Web file I/O examples
# https://www.pythontutorial.net/python-basics/python-read-text-file/

# Title
# Code for Bold face text
start = "\033[1m"
end = "\033[0;0m"
print(start + '\nCh07 How to work with file IO' + end)
print(start + 'How to work with a list in a text file' + end)
print(start + "How to write and read a list of strings" + end)

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
print('-' * 60)
print('members = ["John Clesse", "Eric Idle"]')
print('with open("members.txt", "w") as file: ')
print(sp1 + 'for m in members:')
print(sp2 + 'file.write(f"{m}\\n")                                   # adds new line character')
