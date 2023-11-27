# When and how to use local and global variables
# A function that uses a global constant (okay), Page 115
# Murach's Python programming 2 edition

# Title
# Code for Bold face text
start  = "\033[1m"
end = "\033[0;0m"
print(start + '\nWhen and how to use local and global variables' + end)
print(start + '- A function that uses a global constant (okay) -' + end)
print('-'*60)

# code
print('TAX_RATE = 0.05                     # TAX_RATE is a global constant')
print('def calc_tax(amount):')
print('    tax = amount * TAX_RATE         # the constant is used here')
print('    return tax')
