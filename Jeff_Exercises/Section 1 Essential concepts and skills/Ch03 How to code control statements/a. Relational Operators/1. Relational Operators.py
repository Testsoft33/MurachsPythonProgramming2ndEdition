# Relational Operators Page 67 Chapter 3
# Murach's Python programming 2 edition''

from prettytable import PrettyTable

columns = ['Operator', 'Name', 'Description']

# Specify the column names, while initializing the table
# myTable = PrettyTable({'Operator', 'Name', 'Description'})

# Specify the Column Names while initializing the Table
myTable = PrettyTable(['Operator', 'Name', 'Description'])


# Add rows

myTable.add_row(['==', 'Equal to', 'Returns True if both operands are equal.'])

myTable.add_row(['!=', 'Not equal to', 'Returns True if the left and right operands are not equal.'])
myTable.add_row(['>', 'Greater than', 'Returns True if the left operand is greater than the right operand.'])
myTable.add_row(['<', 'Less than', 'Returns True if the left operand is less than the right operand.'])
myTable.add_row(['>=', 'Greater than or equal to', 'Returns True if the left operand is greater or equal to the right operand.'])
myTable.add_row(['<=', 'Less than or equal to', 'Returns True if the left operand is less than or equal to the right operand.'])


# print myTable
print(myTable)
