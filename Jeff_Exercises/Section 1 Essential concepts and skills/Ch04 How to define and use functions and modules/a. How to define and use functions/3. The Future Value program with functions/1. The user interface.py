# The Future Value program with functions
# The user interface, Page 111
# Murach's Python programming 2 edition

# Code for Bold face text
start  = "\033[1m"
end = "\033[0;0m"

# Title
print('\n' + start + 'The user interface' + end)

# columns = ['Example', 'Comment']
print('-'*60)

string1 =  ('Enter montly investment:            100')
string2 = ('Enter yearly interest rate:         12')
string3 = ('Enter number of years:              10')
string4 = ('Future value:                       33233.91')
string5 = ('Continue?  (y/n): y')

# Print table
print('{}\n{}\n{}\n{}\n\n{}'.format(string1,string2,string3,string4,string5))