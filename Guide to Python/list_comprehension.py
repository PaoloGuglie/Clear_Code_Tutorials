

my_list = [(num, 100 - num) for num in range(0, 100) if num > 75]

print(my_list)

print("\n------------------------------\n")

# If I want to use an else statement, I have to move the if-else

my_list = [(num * 2, num) if num < 20 else 0 for num in range(0, 100)]

print(my_list)

print("\n------------------------------\n")


# I can use list comprehensions with zip()

inventory_names = ['Screws', 'Wheels', 'Metal parts',
                   'Rubber bits', 'Screwdrivers']

inventory_numbers = [43, 12, 95, 421, 23]

selected_items = [(name, number) for name, number in
                  zip(inventory_names, inventory_numbers) if number < 25]

# more flexible than simple list(zip(...)) . I can add if-else statements.

print(selected_items)

print("\n------------------------------\n")


# I can combine list comprehensions

combined_comp = [[x for x in range(5)] for y in range(10)]

# (I can also use "for x in range(10)", it causes no conflict with the other x)

for i in combined_comp:
    print(i)

print("\n------------------------------\n")


# I can create coordinates

combined_comp = [[(x, y) for x in range(5)] for y in range(10)]

print("COORDINATES")
for i in combined_comp:
    print(i)

# I can notice that x increases on every column, and y increases
# on every row.

print("\n------------------------------\n")

combined_comp = [[(x, y) for x in range(10)] for y in range(9, -1, -1)]

print("CARTESIAN COORDINATES")
for i in combined_comp:
    print(i)


print("\n------------------------------\n")


# Chess board

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

chess_board = [[f'{x}{y}' for y in range(1, 9)] for x in reversed(letters)]

print("CHESS BOARD")
for i in chess_board:
    print(i)

# In the innermost list, I have to have the item that is going to be iterated
# through for each line. In this case, the numbers.
# In the outhermost list, I have to have the item that is going to be constant
# on each line. In this case, the letters.
# Each line has every number from 1 to 8, but only one letter.
