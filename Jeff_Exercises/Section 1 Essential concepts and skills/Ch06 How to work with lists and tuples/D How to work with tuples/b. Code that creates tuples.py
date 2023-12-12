# Ch06 How to work with lists and tuples
# How to work with tuples
#  Code that creates tuples, Page 195
# Murach's Python programming 2 edition

# Code for Bold face text
start = "\033[1m"
end = "\033[0;0m"
print(start + "\nMurach's Python programming 2 edition" + end)
print(start + '\nHow to work with tuples' + end)
print(start + ' Code that creates tuples' + end)
print('-' * 60)

# # elements of section
sp1 = (' '*4)
sp2 = (' '*8)  # 8 spaces
sp3 = (' '*27)  # 26 spaces
sp4 = (' '*33)     # 30 spaces
sp5 = (' '*18)

print(start + 'tuple_name = (item1, item2, ...)' + end)

print('# a tuple of 5 floating-point numbers')
state = (48.0, 30.5, 20.2, 100.0, 48.0)
print('state = (48.0, 30.5, 20.2, 100.0, 48.0)')

# a tuple of 6 strings
print()
herbs = ("lavender", "pokeroot", "chamomile", "valerian", "nettles", "oatstraw")
print('herbs = ("lavender", "pokeroot", "chamomile", "valerian", "nettles", "oatstraw")')

# a tuple that stores the data for a movie
print()
movie = ("Monty Python and the Holy Grail", 1975, 9.99)
print('movie = ("Monty Python and the Holy Grail", 1975, 9.99)')

print()
print(start + 'Code that accesses items in a tuple' + end)
print()
print('herbs[0]', herbs[0], '   # lavender')
print('herbs[-1]', herbs[-1], '   # oatstraw')
print('herbs[1:4]', herbs[1:4], "   # 'pokeroot', 'chamomile', 'valerian'")

print('\nherbs[1] = "red clover"')
print('' + start + "TypeError: 'tuple' object does not support item assignment" + end)

