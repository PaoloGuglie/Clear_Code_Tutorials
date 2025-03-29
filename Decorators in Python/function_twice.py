def double_decorator(func):

    def wrapper():
        func()
        print("----------")
        func()

    return wrapper


def other_decorator(func):

    def wrapper():
        func()
        print("Hello!")
        func()

    return wrapper


@double_decorator
@other_decorator
def func():
    """ First, the other_decorator() function is applied to func(),
    then the resulting code is run twice because of double_decorator().
    Each func() call of double_decorator() is referring to the wrapper()
    function of other_decorator(), which in turn has each func() referring
    to func() itself. """

    print("Function")


func()
