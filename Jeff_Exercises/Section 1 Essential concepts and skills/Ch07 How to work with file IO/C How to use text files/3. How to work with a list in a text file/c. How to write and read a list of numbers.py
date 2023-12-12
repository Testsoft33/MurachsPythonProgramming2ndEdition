# Ch07 How to work with file IO
#  An introduction to file Input Output
#   How to use text files
# How to work with a list in a text file
#  How to write and read a list of numbers  page 211
# Murach's Python programming 2 edition

# Web file I/O examples
# https://www.pythontutorial.net/python-basics/python-read-text-file/

# Title
# Code for Bold face text
start = "\033[1m"
end = "\033[0;0m"
print(start + '\nCh07 How to work with file IO' + end)
print(start + 'How to work with a list in a text file' + end)
print(start + "How to write and read a list of numbers" + end)

# header
sp1 = (' ' * 5)
sp2 = (' ' * 8)
sp3 = (' ' * 16)
sp4 = (' ' * 29)
sp5 = (' ' * 24)
sp6 = (' ' * 22)
sp7 = (' ' * 13)

# Section 1
print('\n' + start + 'How to write and read a list of numbers' + end)
print(sp1 + start + 'How to write the items in a list to a file' + end)
print(sp1 + 'years = [1975, 1979, 1983]')
print(sp1 + 'with open("years.txt", "w") as years_file:')
print(sp2 + 'for year in years:')
print(sp3 + 'years_file.write(f"{year}\\n' + sp3 + '# converts int to str')

print('\n' + start + 'Code:' + end)
years = [1975, 1979, 1983]
with open("years.txt", "w") as years_file:
    for year in years:
        years_file.write(f"{year}\n")
print('The contents of the file is: ', years)

# Section 2
print('\n' + sp1 + start + 'How to read the lines in a file into a list' + end)
print(sp1 + 'years = [ ]')
print(sp1 + 'with open("years.txt") as file:')
print(sp2 + 'for line in file:')
print(sp3 + 'line = line.replace("\\n", " ")')
print(sp3 + 'years.append(int(line))' + sp3 + '# converts str to int')
print(sp1 + 'print(years)')

print(start + "\nThe results that's printed to the console" + end)
print('-' * 40)
print(sp1 + '[1975, 1979, 1983]')
