# The input() function, page 52 - 53  Chapter 2
# Murach's Python programming 2 edition'''

# code that gets string input from the user
first_name =input('Enter your first name: ')
print(f'Hello, {first_name}!')

# Another way to get input from the user
print('\nWhat is your first name?')
first_name = input()
print(f'Hello, {first_name}')

# Code that attempts to get numeric input from the user
score_totat = 0
score = input('\nEnter your score: ')
score_totat += int(score)  # Convert score to int because returns How to code if statements string
print('Score is: ', score_totat)