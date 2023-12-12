#  https://www.geeksforgeeks.org/reading-binary-files-in-python/

# opening the binary file in binary mode as rb(read binary)
f = open("movies.bin", mode="rb")

# reading file data with read() method
data = f.read()

# knowing the type of our data
print(type(data))

# Printing our byte sequenced data
print(data)

# Closing the opened file
f.close()