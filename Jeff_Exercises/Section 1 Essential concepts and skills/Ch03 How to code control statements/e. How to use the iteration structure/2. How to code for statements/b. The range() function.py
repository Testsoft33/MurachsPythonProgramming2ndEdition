# How to code for statements, Chapter 3
#  The range( ) function, page 87
# Murach's Python programming 2 edition

# Code for Bold face text
start = "\033[1m"
end = "\033[0;0m"

# Title
print('\n' + start + ' range( ) function' + end)

# Data
Col1 = "Function"
Col2 = "Description"
print()  # Blank line before table
print(f"{Col1:50s} {Col2}")

# print a line of dashes
print("-" * 80)

# print output
print(f"{'range(stop)':50}{'Return integer values from 0 to the stop value, but'}")
print(f"{'':57}{'not including the stop value'}")
print()
print(f"{'range(start, stop[,  step])':45s}{'Returns integer values from the start value to the stop'}")
print(f"{'':57}{'value, but not including the stop value. If the optional'}")
print(f"{'':57}{'step value is specified, this function increments or'}")
print(f"{'':57}{'decrements the integers by the step value.'}")
