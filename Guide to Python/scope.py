# I can move between scopes with parameters, global and return.
# global is a very easy solution to scope but not a good one. I am supposed
# to use a local scope. Can create confusing code and errors.
# It is best to use return.

print("\n")

a = 10


def func():
    global a
    a += 2
    print(a)


func()

print("\n-------------\n")

a = 10


def func(parameter):
    parameter += 2
    print(parameter)


func(a)

print("\n-------------\n")

a = 10


def func(parameter):
    parameter += 2
    return parameter


a = func(a)

print(a)
