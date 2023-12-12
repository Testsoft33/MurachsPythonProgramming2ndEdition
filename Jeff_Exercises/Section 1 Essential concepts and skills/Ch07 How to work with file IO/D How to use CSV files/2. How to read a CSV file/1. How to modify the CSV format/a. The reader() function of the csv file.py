# Ch07 How to work with file IO
#  An introduction to file Input Output
#   How to use CSV files
#  How to write a CSV files
#   The reader() function of the csv file Page 219
# Murach's Python programming 2 edition

import csv

# Title
# Code for Bold face text
start = "\033[1m"
end = "\033[0;0m"
print(start + '\nCh07 How to work with file IO' + end)
print(start + 'How to use CSV files' + end)
print(start + "How to read a CSV file" + end)
print('-' * 60)
print(start + "The reader() function of the csv file" + end)

# header
sp1 = (' ' * 5)
sp2 = (' ' * 8)
sp3 = (' ' * 15)
sp4 = (' ' * 17)
sp5 = (' ' * 14)
sp6 = (' ' * 31)
sp7 = (' ' * 13)

# Section 1
# Print table
print('\nFunction' + sp4 + 'Description')
print('-' * 87)
print('reader(file)' + sp5 + 'Returns a CSV reader object for the file. This')
print(sp6 + 'reader object get the data from the CSV file')

print(start + '\nHow to read data from a CSV file' + end)
print('with open("movies.csv", mode = "r") as file:')
print(sp1 + 'csvFile = csv.reader(file)')
print(sp1 + 'for lines in csvFile:')
print(sp2 + 'print(lines)')

# Run the code from the web
print(start + '\nCode:' + end)
import csv

with open('movies.csv', mode='r') as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        print(lines)
