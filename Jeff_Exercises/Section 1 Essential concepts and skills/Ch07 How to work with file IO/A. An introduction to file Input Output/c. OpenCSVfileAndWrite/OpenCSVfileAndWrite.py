# Ch07 How to work with file IO
#  An introduction to file Input Output
# OpenCSVfileAndWrite,Page 203
# Murach's Python programming 2 edition
# Web file I/O examples
# https://www.pythontutorial.net/python-basics/python-read-text-file/

# Title
# Code for Bold face text
start = "\033[1m"
end = "\033[0;0m"
print(start + '\nCh07 How to work with file IO' + end)
print(start + 'An introduction to file Input Output ' + end)
print(start + "Open CSV file And Write" + end)


import csv

header = ['Movie', 'Year']
data = [
    ['Monty Python and the Holy Grail', 1975],
    ['Cat on a Hot Tin Roof', 1958],
    ['On the Waterfront', 1954],
    ['Star Wars', 1977],
]

# open the file in write mode
with open('Movies.csv', 'w') as f:

    # create the csv writer
    writer = csv.writer(f)


    # write row to csv file
    # User writer.writerows instead of writerrow, only writes one row
    writer.writerows(data)

# Read new contents after write
print(start + '\nPrint CSV file and add entry:\n' + end)
with open('Movies.csv') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        # check if row empty
        if not(row):
            continue
        print(row)






