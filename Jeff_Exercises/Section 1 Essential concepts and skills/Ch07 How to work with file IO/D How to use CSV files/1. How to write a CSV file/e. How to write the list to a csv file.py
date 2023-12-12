# Ch07 How to work with file IO
#  An introduction to file Input Output
#   How to use CSV files
#  How to write a CSV files
#  How to write the list to a csv file Page 217
# Murach's Python programming 2 edition

import csv

# Title
# Code for Bold face text
start = "\033[1m"
end = "\033[0;0m"
print(start + '\nCh07 How to work with file IO' + end)
print(start + 'How to use CSV files' + end)
print(start + "How to write a CSV files" + end)
print('-' * 60)
print(start + "The writerows() method of the CVS writer object" + end)

# header
sp1 = (' ' * 5)
sp2 = (' ' * 8)
sp3 = (' ' * 13)
sp4 = (' ' * 25)
sp5 = (' ' * 37)
sp6 = (' ' * 7)
sp7 = (' ' * 13)
# Section 1
# Print table

# print('\nMethod' + sp4 + 'Description')
# print('-'*60)
# print('writerows(rows)' + sp3 + 'Writes all specified rows to the file specified by the writer')
# print(sp5 + 'object using the CSV format specified by the writer object.')

movies = [["Monty Python and the Holy Grail", 1975],
          ["Cat on a Hot Tin Roof", 1958],
          ["On the Waterfront", 1954]]

myMovie = "C:\\Users\\tests\\Movies.csv"
with open(myMovie, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(myMovie)
    print(movies)
