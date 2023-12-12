# How to code the selection statement,  Pge 82 - 83, Chapter 3
# The invoice program
#  - The user interface
# Murach's Python programming 2 edition

print('\nThe Invoice Program')

print('-'*60)
# row 1
string1 = 'Enter customer type (r / w) :'
string2 = 'R'


print('{}             {}'.format(string1, string2))
# row 2
string1 = 'Enter invoice total :'
string2 = '250'


print('{}                          {}'.format(string1, string2))
print()              # print blank line
# row 3
string1 = 'Invoice total::'
string2 = '250.00'
print('{}                      {}'.format(string1, string2))
# row 4
string1 = 'Discount percent:'
string2 = '0.2'
print('{}               {}'.format(string1, string2))
# row 5
string1 = 'Discount amount::'
string2 = '50.0'
print('{}              {}'.format(string1, string2))
# row 6
string1 = 'New Invoice total:'
string2 = '200.0'
print('{}               {}'.format(string1, string2))