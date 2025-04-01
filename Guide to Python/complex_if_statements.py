

if True and True and False or True:
    """Python combines all the "and" statements into one block inside the if statement.
    This block can be either True of false. If only one value is False, the entire
    expression is False. Then the resulting expression is evaluated in "or". """

    print("True")

# Same as:

if (True and True and False) or True:
    print("True")

# Other test:

if (True and False) or (False and True):
    print("Hello!")

else:
    print("Goodbye!")


# Exercise:
money_available = 100
hungry = False
bored = True

if money_available > 80 and hungry or bored:
    """ First, Python checks the two statements connected by "and". Then
    it evaluates the resulting boolean in the "or" statement. """
    print("eat something...")
