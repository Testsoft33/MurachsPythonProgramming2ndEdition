# Ch08 How to handle exceptions
#  How to handle a single exception
# How exceptions work
# Code that can cause a ValueError exception ,Page 233
# Murach's Python programming 2 edition

# Title
# Code for Bold face text
start = "\033[1m"
end = "\033[0;0m"

# Title
print(start + '\nCh08 How to handle exceptions' + end)
print(start + 'How to handle a single exception' + end)
print(start + 'How exceptions work' + end)
print('-' * 60)
print(start + "Code that can cause a ValueError exception " + end)

# header
sp1 = (' '*4)
sp2 = (' '*7)
sp3 = (' '*15)
sp4 = (' '*22)
sp5 = (' '*12)

# section 1
print('number = int(input("Enter an integer: "))')
print('print(f"You entered a valid integer of {number}.")')
print('print("Thanks!")')

print('\nCode:')
print('Enter 5 for valid number and five for invalid entry.')
number = int(input("Enter an integer:"))
print(f"You entered a valid integer of {number}")
print('Thanks!')