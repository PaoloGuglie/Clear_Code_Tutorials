test = 'this is a test'
other = [1, 2, 3, 4]


# String
print(test.split())

print(test.split('t'))

print(list(test))
print(tuple(test))

print("\n-----------------\n")


# List

# First, I get a string (''), then the join() method.
# The argument for join() must me a list or tuple with strings.

print(' '.join(str(i) for i in other))
print(' - '.join(str(i) for i in other))

# Methods combination
exercies = str(other).strip('[').strip(']').replace(',', '')
print(exercies)
