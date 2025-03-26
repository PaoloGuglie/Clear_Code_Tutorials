# Everything in Python is an object, including strings, integers...
# Functions are just objects with the __call__() dunder method.

# A method belongs to an object, a function is an object.

test = 'a'

# Use dir() with a string
print(dir(test))

############################################


def second_test():
    pass


print(dir(second_test))

##########################################

third = second_test

print(dir(third))  # same result

###########################################

third.extra_attribute = 10
print(dir(third))  # now the function has another attribute.

##############################################


def add(a, b):
    return a + b


class Test:
    def __init__(self, add_function):
        self.add_function = add_function


test4 = Test(add)

print(test4.add_function(2, 4))
