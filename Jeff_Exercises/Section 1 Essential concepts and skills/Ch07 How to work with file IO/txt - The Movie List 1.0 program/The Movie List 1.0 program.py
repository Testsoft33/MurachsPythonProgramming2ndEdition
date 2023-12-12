# Ch07 How to work with file IO
#  An introduction to file Input Output
#   How to use text files
# How to work with a list in a text file
#  txt - The Movie List 1.0 program Page 213
# Murach's Python programming 2 edition

# Web file I/O examples
# https://www.pythontutorial.net/python-basics/python-read-text-file/

# Title
# Code for Bold face text
start = "\033[1m"
end = "\033[0;0m"
print(start + '\nCh07 How to work with file IO' + end)
print(start + 'How to work with a list in a text file' + end)
print(start + "txt - The Movie List 1.0 program" + end)

# header
sp1 = (' ' * 5)
sp2 = (' ' * 8)
sp3 = (' ' * 16)
sp4 = (' ' * 29)
sp5 = (' ' * 24)
sp6 = (' ' * 22)
sp7 = (' ' * 13)

# Code
FILENAME = "movies.txt"


def write_movies(movies):
    with open(FILENAME, "w") as file:
        for movie in movies:
            file.write(f"{movie}\n")


def read_movies():
    movies = []
    with open(FILENAME) as file:
        for line in file:
            line = line.replace("\n", "")
            movies.append(line)
    return movies


def list_movies(movies):
    for i, movie in enumerate(movies, start=1):
        print(f"{i}. {movie}")
    print()


def add_movie(movies):
    movie = input("Movie: ")
    movies.append(movie)
    write_movies(movies)
    print(f"{movie} was added.\n")


def delete_movie(movies):
    index = int(input("Number: "))
    if index < 1 or index > len(movies):
        print("invalid movie number.\n")
    else:
        movie = movies.pop(index - 1)
        write_movies(movies)
        print(f"{movie} was deleted.\n")


def display_menu():
    print("The Movie List Program")
    print()
    print("COMMAND MENU")
    print("list - list all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program")
    print()


def main():
    display_menu()
    movies = read_movies()
    while True:
        command = input("Command: ")
        if command.lower() == "list":
            list_movies(movies)
        elif command.lower() == "add":
            add_movie(movies)
        elif command.lower() == "del":
            delete_movie(movies)
        elif command.lower() == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.")


if __name__ == "__main__":
    main()
