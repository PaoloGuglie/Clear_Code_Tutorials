# These are special functions that translate strings into Python code:

# I can create new variables from a string.

# If these functions are handled badly, they can allow users to run
# their own code.
# Someone could steal data from my database. For example, I can have
# an input field designed for entering names and process it with eval()
# or exec() for correcting typos... An user could enter code instead of
# a name and access my database.

#################################################


# eval() it's the simplest and less powerful: it can only evaluate code. It
# can run functions and simple operations, but it cannot create new variables.

result = eval('1 + 1')  # returns a value
print(result)

print("-----------")

print(eval('"test".upper()'))

print("-----------")

try:
    eval('if True: print("hello!")')

except SyntaxError:
    print("Invalid syntax!")

print("-----------")

try:
    eval('a = 10')

except SyntaxError:
    print("Invalid syntax!")


print("\n-------------------------------\n")


# exec() it's the more powerful one: it can execute any code. I can create
# variables, run functions...

exec('if True: print("hello!")')

print("-----------")

exec('a = 10')
print(a)


print("\n-------------------------------\n")


# Useful example:

my_string = 'test'

print("using eval():")
for i in ['upper', 'title', 'lower', 'casefold']:
    print(eval(f'my_string.{i}()'))

print("-----------")

print("using exec():")
for i in ['upper', 'title', 'lower', 'casefold']:
    exec(f'print(my_string.{i}())')

print("-----------")

# It is safer to use getattr()

print("using getattr():")
for i in ['upper', 'title', 'lower', 'casefold']:
    print(getattr(my_string, i)())
