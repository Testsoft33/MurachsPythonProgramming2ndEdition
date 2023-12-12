# 1 the syntax for a try statement that catches an exception.py

# Ch08 How to handle exceptions
#  How to handle a single exception
# How to use a try statement to handle one type of exception
# How to handle all exceptions,Page 235
# Murach's Python programming 2 edition

# Title
# Code for Bold face text
start = "\033[1m"
end = "\033[0;0m"

# Title
print(start + '\nCh08 How to handle exceptions' + end)
print(start + 'How to handle a single exception' + end)
print('How to use a try statement to handle one type of exceptions')
print('-' * 60)
print(start + "How to handle all exceptions" + end)

# header
sp1 = (' '*4)
sp2 = (' '*8)
sp3 = (' '*11)
sp4 = (' '*12)
sp5 = (' '*23)

print()
print(sp1 + 'try:')
print(sp3 + 'number = int(input("Enter an integer: "))')
print(sp3 + 'print(f"You entered a valid integer of {number}."')
print(sp1 + 'except:')
print(sp3 + 'print("You entered an invalid integer. Please try again."')
print(sp1 + 'print("Thanks!")')