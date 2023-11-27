# When and how to use local and global variables
# functions that use local variables, Page 115
# Murach's Python programming 2 edition

# Title
# Code for Bold face text
start  = "\033[1m"
end = "\033[0;0m"
print(start + '\nWhen and how to use local and global variables' + end)
print(start + '- functions that use local variables -' + end)
print('-'*60)

# code
print('calc_tax(amonut, tax_rate):')
print('\ttax = amonut * tax_rate         # tax is a local variable')
print('\treturn tax                      # return statement is necessary')

print('\ndef main():')
print('\ttax = calc_tax((85.0, .05))     # tax is a local variable')
print('\tprint("Tax:", tax)              # tax 4.25')



