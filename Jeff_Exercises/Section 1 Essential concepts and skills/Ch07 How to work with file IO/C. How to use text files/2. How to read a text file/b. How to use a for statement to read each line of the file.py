# Ch07 How to work with file IO
#  How to use text files
#   How to read a text file
#  How to use a for statement to read each line of the file editor 209
# Murach's Python programming 2 edition

# Web file I/O examples
# https://www.pythontutorial.net/python-basics/python-read-text-file/

# Title
# Code for Bold face text
start = "\033[1m"
end = "\033[0;0m"
print(start + '\nCh07 How to work with file IO' + end)
print('How to use text files')
print(start + 'How to read a text file' + end)
print('-'*60)
print(start + "How to use a for statement to read each line of the file" + end)

# header
sp1 = (' '*5)
sp2 = (' '*10)
sp3 = (' '*27)
sp4 = (' '*29)
sp5 = (' '*24)
sp6 = (' '*22)
sp7 =(' '*13)
# Section 1
# Print table

print( 'with open("members.txt") as file:')
print(sp1 + 'for line in file:')
print(sp2 + 'print(line, end=" ")')
print(sp1 + 'print()')