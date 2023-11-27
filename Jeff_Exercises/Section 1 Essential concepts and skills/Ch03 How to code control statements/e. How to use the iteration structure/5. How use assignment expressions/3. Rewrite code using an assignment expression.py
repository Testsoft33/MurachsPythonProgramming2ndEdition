# How use assignment expressions
#  A while statement that uses an infinite loop to process user data, Page 93
# Murach's Python programming 2 edition

# Code for Bold face text
start  = "\033[1m"
end = "\033[0;0m"

# Rewrite code using an assignment expression
# Title
print('\n' + start + 'How to rewrite code using an assignment expression' + end)
print()

# code
print('Enter -1 to quit.')
print('==============')
while (score := input('Enter a score: ')) != '-1':
    print(f'Youe entered {score}')
print('Bye!')