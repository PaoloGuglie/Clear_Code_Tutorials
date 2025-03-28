import time


# Decorator
def decorator(func):
    """ decorator = wrapper + function generator """

    def wrapper():
        print("decoration begins")
        func()
        print("decoration ends")

    return wrapper


# Basic function to decorate
def func():
    print("Function!")


# overwrite the original function name, giving it new functionality.
# This is the basic idea of a decorator
func = decorator(func)
func()

####################################################
print("--------------")

# Instead of writing func = decorator(func), I can use the decorator shorthand
# (@) right before the decorated function.
# The decorator must have the same name as the decorator function.


@decorator
def func():
    """ Wrap this function inside a decorator """

    print('Function')


func()

##########################################
print("---------------------------")


def duration(func):

    def wrapper():
        start_time = time.time()
        func()
        duration = time.time() - start_time
        print(f"Duration: {duration}")

    return wrapper


@duration
def second_func():
    time.sleep(1)


second_func()
