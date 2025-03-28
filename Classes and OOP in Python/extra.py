# Private attributes : attributes inside a class that cannot be influenced
# outiside of the class (ex. an ID number). This is not possible in Python, so
# developers developed an idea. I create an attribute that starts with "_",
# like "_id". By convention, it's not supposed to be changed. It still can
# be done.
# I can do the same with methods.

# hasattr() and setattr(): they allow to check if a class has an attribute
# and set it.
# hasattr() has two arguments: an object and a string with an attribute name. It
# returns a boolean.
# setattr() has three arguments: an object, a string with an attribute name and
# a new value. Is the same as calling:
#       object.new_attribute_name = new_attribute_value
# This kind of redundance allows me to be efficient (see example in code below).

# doc string: explain what my object does:
#       object.__doc__
# It returns a string. To avoid returning None, I have to create a doc string for
# my object. It is done before the __init__() method with the three quotation
# marks per side string. Used to explain code to other people.

# I can also use the doc string with methods and functions.

# The help() function allows me to see an object's parameters, docstring, methods...
# I can use help() with functions and methods also.


class Monster:
    """ A monster that has some attributes """

    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

        # Private attributes
        self._id = 5

    def attack(self, amount):
        """ The monster attacks and loses energy """
        print("The monster has attacked!")
        print(f"{amount} damage was dealt.")

        self.energy -= 20

    def move(self, speed):
        print("The monster has moved.")
        print(f"It has a speed of {speed}.")


def my_sum(x, y):
    """ Guess what it does... """
    return x + y


monster = Monster(20, 20)

# hasattr()
print(hasattr(monster, 'health'))
print(hasattr(monster, 'weapon'))

print("-----------")

# setattr()
setattr(monster, 'type', 'Skeleton')
print(monster.type)

print("------------")

# Efficient use of setattr()
new_attributes = (['weapon', 'Axe'], ['armor', 'Shield'], ['potion', 'mana'])

for attribute, value in new_attributes:
    setattr(monster, attribute, value)

# doc string
print(monster.__doc__)
print(monster.attack.__doc__)

print(my_sum.__doc__)

# help()
help(monster)
help(monster.attack)
help(my_sum)
