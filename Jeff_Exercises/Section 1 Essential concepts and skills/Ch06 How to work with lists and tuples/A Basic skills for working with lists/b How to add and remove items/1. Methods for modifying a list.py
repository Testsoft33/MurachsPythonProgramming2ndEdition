# Ch06 How to work with lists and tuples
# Basic skills for working with lists
# Use repetition operator asterisk to create a list., Page 165
# Murach's Python programming 2 edition

from tabulate import tabulate

# Title
# Code for Bold face text
start = "\033[1m"
end = "\033[0;0m"
print(start + '\nCh06 Basic skills for working with lists' + end)
print(start + 'How to add and remove items' + end)
print('-' * 60)
print(start + "Methods for modifying a list." + end)
print()

# row 1
string1 = (start + 'append(item)' + end)
string2 = 'Appends the specified item to the end of the list. This increases'
# # columns = ['Example', 'Comment']
# print('{}                     {}'.format('Method', 'Description'))
# print('-'*60)

sp1 = (' ' * 15)
sp2 = (' ' * 27)
sp3 = (' ' * 7)
string3 = 'the length of the list by one.'
string4 = (start + 'insert(index,  item)' + end)
string5 = 'Inserts the specified item at the specified index. This increases'
string6 = 'the length of the list by one and shifts all items after the specified'
string7 = 'index back by one index.'
string8 = (start + 'remove(item)' + end)
string9 = 'Removes the first item in the list that is equal to the specified'
string10 = 'item. This decreases the length of the list by one and shifts all'
string11 = "items after the found item's index forward. If item isn't found "
string12 = "the method raises a ValueError"
string13 = (start + 'index(itme)' + end)
string14 = 'Returns the index of the first occurrence of the specified item in'
string15 = "the list. If the item isn't found, this method raises a ValueError"
string16 = (start + 'pop([index])' + end)
string17 = 'If no index argument is specified, this method gets the last item'
string18 = 'from the list and removes it. Otherwise, this method gets the item'
string19 = 'at the specified index and removes it.'

# Create data
data = [[string1, string2],
        ['', string3],
        [string4, string5],
        ['', string6],
        ['', string7],
        [string8, string9],
        ['', string10],
        ['', string11],
        ['', string12],
        [string13, string14],
        ['', string15],
        [string16, string17],
        ['', string18],
        ['', string19]
        ]

# define header names
col_names = ["Method", "Description"]

# # Print table
# print('{}{}{}\n{}{}\n{}{}{}\n{}{}\n{}{}\n{}{}{}\n{}[}{}'.format(
#     string1,sp1,string2,sp2,string3,string4,sp3,string5,sp2,string6,sp2,
#     string7,string8,string9,string10, string11,string12))

print(tabulate(data, headers=col_names))
