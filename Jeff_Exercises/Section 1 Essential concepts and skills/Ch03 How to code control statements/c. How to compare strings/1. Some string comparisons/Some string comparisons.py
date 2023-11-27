# Some string comparisons Pge 71 Chapter 3
# Murach's Python programming 2 edition

# Title
print('\nSome string comparisons')
print()

# columns = ['Example', 'Comment']
print()  # Print blank line
print('{}                           {}'.format('Condition', 'Boolean result'))
print('-'*60)
# row 1
string1 = '"apple"  < "Apple"'
string2 = ("apple"  <  "Apple")      # evaluates to False
print('{}               {}'.format(string1, string2))
# row 2
string1 = '"App"  <  "Apple"'
string2 =  ("App"  <   "Apple")         # evaluates to True
print('{}                {}'.format(string1, string2))
# row 3
string1 = '1  < 5'      # evaluates to True
string2 =  'True'
print('{}                                  {}'.format(string1, string2))
# row 4
string1 = '"10"  <  "5"'
string2 =  ("10" < "5")         # evaluates to True
print('{}                          {}'.format(string1, string2))
