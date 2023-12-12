# How to code the selection statement,  Pge 79, Chapter 3
# Pseudocode for planning customer discounts
# Murach's Python programming 2 edition
start = "\033[1m"
end = "\033[0;0m"
print(start + 'pseudocode for planning customer discounts' + end)
print('\nGet customer type')
print(start + 'IF' + end + ' type = ' + start + 'R' + end)
print('\t\t' + start + 'IF' + end + ' invoice total  <  250')
print('\t\t\t\t\tdiscount  =  0')
print('\t\t' + start + 'ELSE IF' + end + ' invoice total  >=  250')
print('\t\t\t\tdiscount = 20%')
print(start + 'ELSE IF' + end + ' type = ' + start + 'W' + end)
print('\t\tdiscount  =  40%')
print(start + 'ELSE' + end)
print('\t\tprint invalid type message')
