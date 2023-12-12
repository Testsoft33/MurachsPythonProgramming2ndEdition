# Following syntax to create tables
# print(tabulate(data, headers=col_names, tablefmt="grid",
#     showindex="always"))

from tabulate import tabulate

# create data
data = [["    ", "      Main              ", "  ", "  "],
        ["display menu", "list movies", "add movies", "delete movie"]
        ]

# define header names
# col_names = ["The hierarchy chart"]
print('\n' + ('  ' * 18) + 'The hierarchy chart')

align = ["left"]

table = tabulate(data, tablefmt="fancy_grid", colalign=align)

# display table
# print(tabulate(data, headers=col_names))
print(table)
