import my_module

print(my_module.test_var)

my_module.test_function(123)

my_object = my_module.MyClass('John', 5)

my_object()

print("\n------------------------\n")


# When a Python file is called, it creates a few internal variables: __name__
# is one of them. It gives a name to the python file.
# Python assigns the name '__main__' to the file I am executing when I run
# a program.
# Any imported file is called 'filename'.
# Useful to control what code is executed and avoiding executing code by accident

print(f"Executed file: {__name__}")

# Usually, it's used with an if statement:

if __name__ == '__main__':
    print("AAA")

# This makes sure that this print statement is run only if this is the file I
# am executing.
