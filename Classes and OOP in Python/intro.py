# Variables in an object are called ATTRIBUTES.
# Functions in an object are called METHODS.

# I can add an object inside another object as an attribute.

# A CLASS is a blueprint for an object. When creating an OBJECT, I first need a class.

# A class can inherit from another class. The resulting objects will have attributes
# and methods from both classes.

# By convention, class names are written in CamelCase.
# Variable names are written in snake_case.

# Whenever I call a method, Python automatically passes a reference to the class as
# the first argument into the method. I have to capture it with a PARAMETER. This
# means that a method needs at least one parameter, as a reference to the class
# itself. Usually "self" is used, but I can also use other words.
# I can add as many parameters as I want.


class Monster:

    # Attributes
    health = 90
    energy = 40

    # Methods
    def attack(self):
        print("The monster has attacked!")

    def other_attack(monster, amount):
        """ Used "monster" instead of "self" """

        print(f"{amount} damage was dealt.")
        print(monster.energy)

        # decrease energy
        monster.energy -= 20
        print(monster.energy)

    def move(self, speed):
        print(f"The monster has moved at {speed} km/h.")


# create an object (instance of a class)
monster = Monster()

print(monster.health, monster.energy)

monster.attack()
monster.other_attack(40)

monster.move(5)
