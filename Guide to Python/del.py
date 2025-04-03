# To delete variables:

my_var = 2

print(my_var)

del my_var

try:
    print(my_var)

except NameError:
    print("It does not exist!")

print("\n--------------------------------\n")


# Most of the time, I only delete values inside of lists.
# In this case "del" removes items by index.

my_list = [1, 2, 'hello', 4]

del my_list[1]

print(my_list)

print("\n--------------------------------\n")


# I can remove an item BY VALUE:

my_list = [1, 2, 'hello', 4]

my_list.remove('hello')

print(my_list)

print("\n--------------------------------\n")


# The .pop() method removes an itex BY INDEX.
# The default values is -1

my_list = [1, 2, 'hello', 4]

print(f"My list: {my_list}")

print(f"Removed item: {my_list.pop()}")

print(f"New list: {my_list}")

print("-------------------")

my_list = [1, 2, 'hello', 4]

print(f"My list: {my_list}")

print(f"Removed item: {my_list.pop(0)}")

print(f"New list: {my_list}")

# Instead of .remove(), .pop() returns the deleted value

print("\n--------------------------------\n")


# I can clear the entire list

my_list = [1, 2, 'hello', 4]

my_list.clear()

print(my_list)
