# To explain what a function does, I can add a docstring at the
# beginning of a function.

def test(a, b):
    """ A simple function that prints 2 parameters """

    print(f"First: {a}\nSecond: {b}")


test(1, 2)

print("\n---------------------\n")

# I can use the .__doc__ to get the docstring.
print(test.__doc__)

print("\n---------------------\n")

# I can use the help() function to see everything about the function.

help(test)

print("\n---------------------\n")


# I can hint what I am expecting for the parameters (:) and what the function
# should return (->):

def test(a: int, b: int) -> int:
    """ A simple function that prints 2 parameters """

    print(f"First: {a}\nSecond: {b}")

    return a + b


help(test)

print("\n---------------------\n")


# I can also add a default parameter:

def test(a: int = 4, b: int = 2) -> int:
    """ A simple function that prints 2 parameters """

    print(f"First: {a}\nSecond: {b}")

    return a + b


help(test)

tot = test()
print(f"My sum is {tot}")
