def repetition_decorator(repetitions):
    """ 1) I call the repetition decorator and pass 5.
    2) This creates a new decorator() function and return it.
    All I get from repetition_decorator() is decorator().
    decorator() replaces all of repetition_decorator(5).
    3) On this new decorator I am calling the new function,
    meaning now I am passing func() into the decorator()
    as parameter.
    4) Now I am back to a normal decorator, returning wrapper().
    5) wrapper() is stored inside func(). """

    def decorator(func):

        def wrapper():
            for i in range(repetitions):
                func()

        return wrapper

    return decorator


# This...
@repetition_decorator(5)
def func():
    print('function')


# ... is the same as this:
func = repetition_decorator(5)(func)   # becomes func = decorator(func)

func()
