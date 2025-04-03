# Besides sorted, map() and filter() also sort data.
# These have mostly been replaced by list comprehensions.

my_list = [1, 2, 3, 4, 5]

# map(key, iterable) changes values with a function inside an iterable.

# It cycles through the list and every value is passed into a function.
# A new list is created with the returned values from the function.


def func(i):
    """ Modify each item """
    return i ** 2


mapped_list = list(map(func, my_list))

print(mapped_list)

print("\n----------------------\n")


# filter(key, iterable) filters out values form a condition.

# It cycles through the list and every value is passed into a function.
# Depending on the return from the function, the value either stays in the
# list or gets filtered out (truthy/falsy values).


def func(i):
    """ Filter some items from the iterable """

    if i < 4:
        return True

    else:
        return False


filtered_list = list(filter(func, my_list))

print(filtered_list)

print("\n----------------------\n")


# I can always use lambda functions:

print(list(map(lambda x: x ** 2, my_list)))
print(list(filter(lambda x: x < 4, my_list)))
print(list(filter(lambda x: x % 2, my_list)))

print("\n----------------------\n")


# I can convert everything into list comprehensions:

print([i ** 2 for i in my_list])
print([i for i in my_list if i < 4])
print([i for i in my_list if i % 2])
