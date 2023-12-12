# Ch06 How to work with lists and tuples
# How to create a list of lists
#  How to loop through the rows and columns of a two-dimensional list, page 185
# Murach's Python programming 2 edition


# Code for Bold face text
start = "\033[1m"
end = "\033[0;0m"
print(start + '\nCh06 Basic skills for working with lists' + end)
print(start + 'More skills for working with lists' + end)
print(start + 'How to count, reverse, and sort items in a list' + end)
print('-' * 60)
print(start + 'Three more list methods' + end)

# # elements of section
sp1 = (' ' * 4)
sp2 = (' ' * 8)  # 8 spaces
sp3 = (' ' * 19)  # 26 spaces
sp4 = (' ' * 27)  # 30 spaces
sp5 = (' ' * 38)
print()

print('Method' + sp4 + 'Description')
print('-' * 60)
print(start + 'count(item)' + end + sp3 + 'Returns the number of occurrences of an item the list. If')
print(sp5 + "the item isn't found in the list, this method returns 0.")
print(sp5 + 'Reverse the order of the items in the list.')
print(start + 'reverse(list)' + end + sp3 + 'Reverses the order of the items in the list.')
print(start + 'sort(key=function)' + end + sp2 + 'Sorts the list items in place. The optional key argument.')
print(sp5 + 'specifies a function to be called on each item before sorting.')
