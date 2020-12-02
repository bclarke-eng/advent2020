import re

# DAY 1

# Reads in the data and converts it to a list of numbers
with open("data1.txt", "r") as f:
    num_list = [int(number) for number in f.read().split()]

# Part 1
# Finds two different numbers in the data that add to 2020 and prints their product
print("Multiple for 2 numbers:", [x * y for i, x in enumerate(num_list) for j, y in enumerate(num_list) if (i != j and x + y == 2020)][0])

# Part 2
# Finds three different numbers in the data that add to 2020 and prints their product
print("Multiple for 3 numbers:", [x * y * z for i, x in enumerate(num_list) for j, y in enumerate(num_list) for k, z in enumerate(num_list) if (i != j != k and x + y + z == 2020)][0])
# -------------------------------------------------------------------------------------------------------

# DAY 2

# Reads in the data and converts it to a list of passwords with policies
with open("data2.txt", "r") as g:
    password_list = [password for password in g.read().splitlines()]

old_valid_passwords = 0
new_valid_passwords = 0

for word in password_list:
    # Regex search to find needed information
    list_item = re.findall(r"^(\d{1,})(-)(\d{1,})( )(\w)(: )(\w+)$", word)[0]
    policy_min_number = int(list_item[0])
    policy_max_number = int(list_item[2])
    policy_letter = list_item[4]
    pass_word = list_item[6]

    # Part 1
    if policy_min_number <= pass_word.count(policy_letter) <= policy_max_number:
        old_valid_passwords += 1

    # Part 2
    password_letters = list(pass_word)
    if (password_letters[policy_min_number - 1] == policy_letter and password_letters[policy_max_number - 1] != policy_letter) \
            or (password_letters[policy_min_number - 1] != policy_letter and password_letters[policy_max_number - 1] == policy_letter):
        new_valid_passwords += 1

print("Number of old valid passwords:", old_valid_passwords)
print("Number of new valid passwords:", new_valid_passwords)
