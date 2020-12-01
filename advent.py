# Reads in the data and converts it to a list of numbers
with open("data.txt", "r") as f:
    num_list = [int(number) for number in f.read().split()]

# Finds two different numbers in the data that add to 2020 and prints their product
print([x * y for i, x in enumerate(num_list) for j, y in enumerate(num_list) if (i != j and x + y == 2020)][0])

# Finds three different numbers in the data that add to 2020 and prints their product
print([x * y * z for i, x in enumerate(num_list) for j, y in enumerate(num_list) for k, z in enumerate(num_list) if (i != j != k and x + y + z == 2020)][0])
git