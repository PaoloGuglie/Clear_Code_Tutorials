from time import time, sleep


def transform(func):

    def wrapper():
        print("transform() begins")
        print("------")
        func()
        print("------")
        print("transform() ends")

    return wrapper


def duration(func):

    def wrapper():
        print("duration() begins")
        print("------")
        start_time = time()
        func()
        duration = time() - start_time
        print("---------")
        print("duration() ends")
        print(f"Duration: {duration}")

    return wrapper


@transform
@duration
def func():
    """ 1) The transform() function prints its first lines.
    2) Control is passed to the duration() function, which
    is passed to transform() as argument.
    3) The duration() function starts keeping track of time.
    4) Control is passed to the func() function, which is passed
    to duration() as argument.
    5) The func() function prints a line and stops the program
    for 1 second.
    6) Control is passed back to the duration() function.
    7) The duration() function prints the time.
    8) Control is passed back to the transform function().
    9) The transform() function prints the last two lines

    Nesting structure:

    transform():
    -----------
        duration()
        -------------
            func()
            ---------------
        duration()
        -------------
    transform()
    -----------"""

    print("func()")
    sleep(1)


func()
