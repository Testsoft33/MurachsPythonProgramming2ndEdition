# Ch08 How to handle exceptions
#  How to handle a single exception
# How exceptions work
# Two functions that can cause a ValueError exception,Page 233
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
print(start + "Two functions that can cause a ValueError exception" + end)

# header
sp1 = (' '*4)
sp2 = (' '*7)
sp3 = (' '*15)
sp4 = (' '*12)
sp5 = (' '*23)

print('\nFunction' + sp3 + 'Reason for exception')
print('-'*90)
print('int(data)' + sp3 + "Can't convert the data arguments to an int value.")
print('float(data)' + sp4 + "Can't convert the data argument to a float value.")