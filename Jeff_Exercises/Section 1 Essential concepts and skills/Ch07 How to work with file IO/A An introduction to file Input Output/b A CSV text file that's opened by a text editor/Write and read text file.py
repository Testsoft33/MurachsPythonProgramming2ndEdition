# Read file before writing
print('\nExample 2;')
with open('Movies.txt') as f:
    for line in f:
        print(line.strip())
f.close()

# Write file
print('Write to the file: ')
lines = ['Readme', 'How to write to a txt file']
with open('Movies.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')
f.close()

# read file
# More concise code
print('\nExample 2;')
with open('Movies.txt') as f:
    for line in f:
        print(line.strip())
f.close()

# write the contents back
print('Write the contents back')
lines = ["Monty Python and the Holy Grail", "1975", "Cat on a Hot Tin Roof", "1958", "On the Waterfront", "1954",
         "Eric Idle"]
with open('Movies.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')
f.close()

# Read file before writing
print('\nExample 2;')
with open('Movies.txt') as f:
    for line in f:
        print(line.strip())
f.close()
