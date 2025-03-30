# I can have functions with parameters being decorators.

# Decorators can also have parameters. It is complicated because I would
# be wrapping a function inside a function inside another function.

def decorator(func):

    def wrapper():
        """ In calling wrapper(), the function's argument
        is "forgotten" """

        print("Decorator begins.")
        func()
        print("Decorator ends.")

    return wrapper


@decorator
def func(func_parameter):
    print(func_parameter)


try:
    func('hello')

except TypeError:
    print("Error!")

# I will now get an error because the function func() needs a parameter, but
# in the decorator func() is called without arguments.
print("------------------")


# Correct code:

def decorator(func):
    """ Added wrapper parameter used as function argument """

    def wrapper(wrapper_parameter):
        print("Decorator begins.")
        func(wrapper_parameter)
        print("Decorator ends.")

    return wrapper


@decorator
def func(func_parameter):
    print(func_parameter)


func('something...')


# I can have this to have the decorator accept any kind of function with any
# kind of parameter:
def decorator(func):

    def wrapper(*args, **kwargs):
        print("decoration begins")
        func(*args, **kwargs)
        print("decoration ends")
