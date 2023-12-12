# 1 the syntax for a try statement that catches an exception.py

# Ch08 How to handle exceptions
#  How to handle a single exception
# How to use a try statement to handle one type of exception
# The syntax for a try statement that catches an exception,Page 235
# Murach's Python programming 2 edition

# Title
# Code for Bold face text
start = "\033[1m"
end = "\033[0;0m"

# Title
print(start + '\nCh08 How to handle exceptions' + end)
print(start + 'How to handle a single exception' + end)
print('-' * 60)
print(start + "The syntax for a try statement that catches an exception" + end)

# header
sp1 = ' '*4
sp2 = ' '*8
sp3=' '*12
sp4 = ' '*12
sp5 = ' '*23

print()
print(sp1 + 'try:')
print(sp3 + 'statements')
print(sp1 + 'except  [ExceptionName]:')
print(sp3 + 'statements')