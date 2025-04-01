# List unpacking

def print_all(first, *args):
    print(f"First number: {first}")

    print("Others:", end=' ')
    last_arg = args[-1]

    for i in args:
        print(i, end=(', ' if i is not last_arg else ''))


print_all(2, 33, 5, 7)

print("\n\n-----------\n")


# Keyword unpacking: looks for keyword arguments and unpacks them into
# a dictionary.

def print_more(**kwargs):
    print(kwargs)


print_more(arg1=1, arg2='test', arg3=[2, 5, 6])

print("\n-----------\n")


# Combine them together:

def print_even_more(*args, **kwargs):
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")


print_even_more()
print("------")
print_even_more(2, 5, 734, 24, 'hello', test=2, man=True, zoo='animals')

print("\n-----------\n")


# Exercise:

def calculator(*args):
    print(f"Sum: {sum(args)}")


calculator(3, 65, 1000)
