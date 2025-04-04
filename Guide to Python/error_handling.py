# Basic try/except error handling:

print("-------------------------\n")

try:
    print(1 / 0)

except:
    print('error!')

print("\n-------------------------\n")

try:
    print(1 / 1)

except:
    print('error!')

print("\n-------------------------\n")


# I can be more specific:

try:
    print(a)

except NameError:
    print("This does not exist!")

try:
    print(1 / 0)

except ZeroDivisionError:
    print("Cannot divide by 0!")


# In this case, as soon as the line 'print(a)' is read, the program jumps
# to the NameError exception. None of the stuff below is executed.

print("\n-------------------------\n")


# In this case, as soon as the line 'print(a)' is read, the program jumps
# to the NameError exception. None of the stuff below is executed.

try:
    print(a)
    print(1 / 0)

except ZeroDivisionError:
    print("Cannot divide by 0!")

except NameError:
    print("This does not exist!")

print("\n-------------------------\n")


# I can also use the "else" statement. It is only run if the "try" statement
# does not have an error.
# It is an else to the "except" statements.

try:
    print("try")

except ZeroDivisionError:
    print("Cannot divide by 0!")

except NameError:
    print("This does not exist!")

else:
    print("something else...")

print("\n-------------------------\n")


# I can also have "finally". It runs either way at the end.
# It doesn't matter if there's an exception or not.

try:
    print("try")

except NameError:
    print("This does not exist!")

else:
    print("something else...")

finally:
    print("finally!")

print("\n-------------------------\n")


try:
    print(1 / 0)

except ZeroDivisionError:
    print("Cannot divide by 0!")

else:
    print("something else...")

finally:
    print("finally!")

print("\n-------------------------\n")


# I can raise my own errors.

var_must_be_string = 'my string'

if isinstance(var_must_be_string, str):
    print(var_must_be_string)

else:
    raise TypeError('Must be a string!')

print("-------------")

var_must_be_string = 3

if isinstance(var_must_be_string, str):
    print(var_must_be_string)

else:
    raise TypeError('Must be a string!')

print("\n-------------------------\n")


# I can also use "assert" to make sure my code only runs if a certain
# condition is true. It's a strongef if statement. If the condition is
# false, my entire code stops with an AssertionError.

a = 6

assert a == 5

# Useful while working with something security concerned.
