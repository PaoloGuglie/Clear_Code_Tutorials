# Lambda functions are simple single line functions

a = lambda x: x + 1

print(a(10))


simple_calculator = lambda a, b: a + b

print(simple_calculator(2, 3))


# They are used when some functions want other function as argument
# For example sort() can accept functions to order.

# They are used in GUIs where every button gets a lambda function to
# execute basic commands.


# Exercise
greet = lambda x: 'hello' if x > 5 else 'bye'


print(greet(2), greet(8))
