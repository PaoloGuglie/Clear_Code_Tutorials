# I want to get items sorted by index from these:

inventory_names = ['Screws', 'Wheels', 'Metal parts',
                   'Rubber bits', 'Screwdrivers']

inventory_numbers = [43, 12, 95, 421, 23]


# With a normal for loop, I need the enumerate() function:

for index_name, name in enumerate(inventory_names):
    for index_num, num in enumerate(inventory_numbers):
        # print only when same index is encountered
        if index_name == index_num:
            print(f"{name}: {num}")
            # skip useless couples
            break

print("\n-----------------------------\n")


# Using list(zip(list1, list2)), I create a list of tuples.
# Each tuple is a combination of two items, one from each list,
# sorted by the index.

print(list(zip(inventory_names, inventory_numbers)))

print("\n-----------------------------\n")

# I can use zip() to get the sorted items:

for i in zip(inventory_names, inventory_numbers):
    print(f"{i[0]}: {i[1]}")

print("\n-----------------------------\n")


# A better way to write it:

for name, number in zip(inventory_names, inventory_numbers):
    print(f"{name}: {number}")

print("\n-----------------------------\n")


# Combining zip() with enumerate(), I get tuples. In each tuple, the
# first value is the index of the tuple and the second is a tuple
# from the zip() function.
# Makes sense: each zip() tuple is the "item" to use enumerate() on.

for i in enumerate(zip(inventory_names, inventory_numbers)):
    print(i)

print("\n-----------------------------\n")

# unpacking this:
for index, item_pair in enumerate(zip(inventory_names, inventory_numbers)):
    print(f"{item_pair[0]} [id: {index}] - inventory: {item_pair[1]}")
