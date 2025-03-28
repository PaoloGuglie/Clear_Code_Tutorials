# Decorators are functions that decorate other functions. We wrap one function
# around another function. Inside the decorator function I am calling the
# original function. I execute code before and after the function.
#       func(func())
# This way I can give a function extra functionality without changing it. For
# example, I can create a decorator for a function that makes the function
# execute twice when called.

# I usually see decorators in three different circumstances:
# 1) I want to test my code without changing it.
# 2) I work in a team and I want to avoid making unnecessary changes.
# 3) Using a decorator inside a class allows me to run code when an
# attribute is accessed or changed.

# Remember that functions are objects and can be passed around.

def func():
    print("Function!")


def wrapper(function):
    """ This is basically the main idea of a decorator"""

    print("before")
    function()
    print("after")


wrapper(func)

print("--------------------")


def function_generator():
    """ Generate a function inside a function """

    def new_function():
        print("New function")

    return new_function


new_function = function_generator()
new_function()

print("-----------------")
