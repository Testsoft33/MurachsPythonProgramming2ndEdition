# How to use the iteration structure,  Pages 84 -95, Chapter 3
# A while loop that prints the numbers 0 through 4 to the console, page 85
# Murach's Python programming 2 edition

# Code for Bold face text
start = "\033[1m"
end = "\033[0;0m"

# Title
print(start + '\nCode that causes an infinite loop' + end)
print()

# code
counter = 0
while True:
    print('Loop will not end until Ctrl + C pressed!!!', counter)
    counter += 1
