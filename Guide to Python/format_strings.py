# First method:

name = 'Tom'
age = 40

greetings = 'Hello {}, you are {} years old.'.format(name, age)

print(greetings)


# Second method:

greetings = 'Hello {one}, you are {two} years old.'.format(one=name, two=age)

print(greetings)


# Third method:

greetings = f'Hello {name}, you are {age} years old.'

print(greetings)
