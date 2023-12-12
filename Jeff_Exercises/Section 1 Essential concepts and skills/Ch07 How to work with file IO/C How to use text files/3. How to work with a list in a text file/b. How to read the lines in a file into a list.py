# Ch07 How to work with file IO
#  An introduction to file Input Output
#   How to use text files
# How to work with a list in a text file
#  How to read the lines in a file into a list page 211
# Murach's Python programming 2 edition

# Web file I/O examples
# https://www.pythontutorial.net/python-basics/python-read-text-file/

# Title
# Code for Bold face text
start = "\033[1m"
end = "\033[0;0m"
print(start + '\nCh07 How to work with file IO' + end)
print(start + 'How to work with a list in a text file' + end)
print(start + "How to read the lines in a file into a list" + end)

# header
sp1 = (' ' * 5)
sp2 = (' ' * 8)
sp3 = (' ' * 16)
sp4 = (' ' * 29)
sp5 = (' ' * 24)
sp6 = (' ' * 22)
sp7 = (' ' * 13)

# Section 1
# Print table
print('-' * 60)
print('members = [ ]')
print('with open("members.txt") as file:')
print(sp2 + 'for line in file:')
print(sp3 + 'line = line.replace("\\n", " ")' + sp3 + '# removes new line character')
print(sp3 + 'members.append(line)')
print('print(members)')

print(start + "\nThe result that's printed to the console")
print('Code:')
members = []
with open("members.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        members.append(line)
print(members)
