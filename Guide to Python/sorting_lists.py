# Regular list sorting:

list1 = [4, 2, 3, 1, 5]

list1.sort()

print(list1)

print(sorted([2, 5, 3, 8, 4]))

print("\n---------------------\n")


# Both function can accept the "reverse" parameter:

list1 = [4, 2, 3, 1, 5]

list1.sort(reverse=True)

print(list1)

print(sorted([2, 5, 3, 8, 4], reverse=True))

print("\n---------------------\n")


# I can also use the "key" parameter, submitting a function:

list2 = [('a', 3), ('b', 10), ('c', 6), ('d', 5)]

# I want to sort this list by the integer in each tuple


def sort_function(item: tuple[str, int]) -> int:
    """ Each tuple is passed inside this function as an argument.
    This function has to return an integer and the size of the
    integer is going to determine the ordering of the list. """

    return item[1]

# The "[]" in tuple[str, int] are used for generic type hints.


list2.sort(key=sort_function)

print(list2)

# I can still use the "reverse" parameter:

list2 = [('a', 3), ('b', 10), ('c', 6), ('d', 5)]

print(f"\nReversed list: {sorted(list2, key=sort_function, reverse=True)}")

print("\n---------------------\n")


# I usually use lambda function as a "key" parameter:

list2 = [('a', 3), ('b', 10), ('c', 6), ('d', 5)]

list2.sort(key=lambda item: item[1])

print(list2)

print("\n---------------------\n")


# Exercise:

names = ['Screws', 'Wheels', 'Metal parts', 'Wood', 'Rubber bits']
numbers = [23, 12, 95, 44, 11]

print("Sorted by item numbers:")
print(sorted(zip(names, numbers), key=lambda x: x[1]))

print("\nSorted by name length:")
print(sorted(zip(names, numbers), key=lambda x: len(x[0])))
