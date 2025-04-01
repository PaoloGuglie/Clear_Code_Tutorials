# Match case is similar to if, but I still run code if a condition is True.
# Used to check for one value out of a long list of values.
# (like switch in C)
# I can only look for perfect matches, cannot use comparison operators.

mood = 'hungry'

match mood:

    case 'thirsty':
        print("get some water!")

    case 'hungry':
        print("get some food!")

    case 'tired':
        print("get some sleep!")

    case _:
        """ like "default" in C switch statement """
        print("any other mood...")
