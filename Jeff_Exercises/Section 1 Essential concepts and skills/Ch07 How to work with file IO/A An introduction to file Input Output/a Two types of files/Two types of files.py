# Ch07 How to work with file IO
#  An introduction to file Input Output
# Two types of files ,Page 203
# Murach's Python programming 2 edition

# Title
# Code for Bold face text
start = "\033[1m"
end = "\033[0;0m"
print(start + '\nCh07 How to work with file IO' + end)
print(start + 'An introduction to file Input Output ' + end)
print('-' * 60)
print(start + "Two types of files" + end)

# header
sp1 = (' ' * 15)
sp2 = (' ' * 7)
print()
print('Type' + sp1 + 'Description')
print('-' * 60)

sp1 = (' ' * 15)
sp2 = (' ' * 22)
sp3 = (' ' * 12)

# section 1
string1 = 'Text'
string2 = 'Contains one or more lines that contain text characters. In a text file, each line'
string3 = 'ends with a new line character (\\n). On Windows, this character is sometimes'
string4 = 'preceded by a carriage return character (\\r).'
string5 = 'Common types include: CSV files, JSON files, XML files, and HTML files.'
string6 = 'Binary'
string7 = "Any file that isn't a text file. Many binary file formats contain parts that can be"
string8 = 'interpreted as text. However, binary files typically contain a sequence of bytes'
string9 = 'that are intended to be interpreted as something other than text characters.'
string10 = 'Common types include compiled program files,  image files, audio files, video'
string11 = 'files, database files, and compressed files.'

print(
    '{}{}{}\n{}{}\n{}{}\n{}{}\n{}{}{}\n{}{}\n{}{}\n{}{}\n{}{}'.format(string1, sp1, string2, sp2, string3, sp2, string4,
                                                                      sp2, string5,
                                                                      string6, sp3, string7, sp2, string8, sp2, string9,
                                                                      sp2, string10, sp2, string11))
