# The Movie List Program
# User interface

# Following syntax to create tables
# print(tabulate(data, headers=col_names, tablefmt="grid",
#     show index="always"))

from tabulate import tabulate

# Code for Bold face text
start = "\033[1m"
end = "\033[0;0m"

# create data
data = [["list - List all movies"], ["add - Add a movie"], ["del - Delete a movie"], ["exit - Exit program"], ["   "],
        [start + "Command: list" + end], ["1. Monty Python and the Holy Grail"], ["2. On the Waterfront"],
        ["3. Cat on a Hot Tin Roof"],
        ["   "], [start + "Command: add" + end], [start + "Name: " + end + "Casablanca"], ["Casablanca was added"],
        ["   "],
        [start + "Command: list" + end], ["1. Monty Python and the Holy Grail"], ["2. On the Waterfront"],
        ["3. Cat on a Hot Tin Roof"],
        ["4. Casablanca"], ["  "], [start + "Command: del" + end], ["Number: 4"], ["Casablanca was deleted"], ["  "],
        [start + "Command: list" + end],
        ["1. Monty Python and the Holy Grail"], ["2. On the Waterfront"], ["3. Cat on a Hot Tin Roof"]]

# define header names
col_names = [start + "COMMAND MENU" + end]

align = ["left"]

# tablefmt can be: simple, grid, fancy_grid
table = tabulate(data, col_names, tablefmt="presto", colalign=align)

# display table
# print(tabulate(data, headers=col_names))
print(table)
