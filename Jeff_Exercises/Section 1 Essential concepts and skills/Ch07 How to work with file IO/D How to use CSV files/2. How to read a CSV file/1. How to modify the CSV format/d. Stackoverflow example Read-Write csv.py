# Example from stackoverflow
#  https://stackoverflow.com/questions/41585078/how-do-i-read-and-write-csv-files

import csv

# Define data
data = [
    (1, "A towel,", 1.0),
    (42, " it says, ", 2.0),
    (1337, "is about the most ",  -1),
    (0, "massively useful thing ", 123),
    (-2, "an interstellar hitchhiker can have. ", 3),
]

# write CSV file
with open("test.csv", "wt") as fp:
    writer = csv.writer(fp, delimiter=",")
    # writer writerow(["your", "header", "foo"]) # write header
    writer.writerows(data)

# Read CSV file
with open("test.csv") as fp:
    reader = csv.reader(fp, delimiter=",", quotechar='"')
    # next(reader, None) # skip the headers
    data_read = [row for row in reader]

print(data_read)