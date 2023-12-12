# Ch06 How to work with lists and tuples
# How to work with tuples
#  A function that returns a tuple Page 195
# Murach's Python programming 2 edition

import random

# Code for Bold face text
start = "\033[1m"
end = "\033[0;0m"
print(start + "\nMurach's Python programming 2 edition" + end)
print(start + '\nHow to work with tuples' + end)
print(start + 'The Number Crunching Program' + end)
print('-' * 60)

# # elements of section
sp1 = (' ' * 4)
sp2 = (' ' * 8)  # 8 spaces
sp3 = (' ' * 27)  # 26 spaces
sp4 = (' ' * 33)  # 30 spaces
sp5 = (' ' * 18)

print('The Code: ')


# TUPLE DATA: (0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50)
# Average = 25 Median = 25 Min = 0 Max = 50 Dupe = []
#
# RANDOM DATA: [4, 6,] 19, 22, 26 ,29, 39, 42, 45, 47]
# Average = 28 Median = 29 Min = 4 Max = 47 Dups = [29]


def get_duplicates(data):
    pass


def crunch_numbers(data):
    total = 0
    for number in data:
        total += number

    average = round(total / len(data))
    median_index = len(data) // 2
    median = data(median_index)
    minimum = min(data)
    maximum = max(data)
    # dups = get_duplicates(data)

    print("Average =", average,
          "Median =", median,
          "Min =", minimum,
          "Max =", maximum,
          "Dups =", dups)

    # def get_duplicates(data):
    #     dups = []
    #     for i in range(51):
    #         count = data.count(i)
    #         if count >= 2:
    #             dups.append(i)
    #     return dups

    def main():
        fixed_tuple = (0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50)
        random_list = [0] * 11
        for i in range(len(random_list)):
            random_list[i] = random.randint(0, 50)
        random_list.sort()

        print("TUPLE DATA:", fixed_tuple)
        crunch_numbers(fixed_tuple)
        print()
        print('RANDOM DATA:', random_list)
        crunch_numbers(random_list)

    # if started as the main module, call the main() function
    if __name__ == "__main__":
        main()
