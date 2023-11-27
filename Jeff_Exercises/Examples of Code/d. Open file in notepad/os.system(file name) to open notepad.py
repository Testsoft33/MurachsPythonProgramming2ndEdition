# Example of opening notepad with import os & os.system command

import os

with open('test.txt', 'w') as outfile:
    # change Quoted string to print another text to text file
    outfile.write("Test\nOpen notepad and show text in Notepad\nChange text for new text!")
 # open notepad and show text written to test.txt file
os.system('test.txt')

 # open notepad and show text written to test.txt file
# os.system('test.txt')