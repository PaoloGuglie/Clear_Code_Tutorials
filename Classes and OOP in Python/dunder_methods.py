# A __Dunder__ (Double UNDERscore) method is a method that is not called by the user,
# but it's called by Python when something happens:
# __init__ is called when the object is created.
# __len__ is called when the object is passed into the len() function.
# __abs__ is called when the object if passed into the abs() function.
# __call__ turns the object into a function.
# __add__ treats the object as a number.
# __str__ treats the object as a string. I can use it with print(str(object))
# or just print(object).

# Every time I create an object, Python already gives it some default dunder
# methods and attributes:
# __dir__ is necessary for the dir() function to work.
# __dict__ is a sort of dictionary. It is an attribute, not a method. It returns
# all the attributes of the object inside a dictionary. I can also use the vars()
# function to return this dictionary.


class Monster:

    # Dunder methods
    def __init__(self, health, energy):

        # assign the given arguments to attributes
        self.health = health
        self.energy = energy

        print("The monster was created!")

    def __len__(self):
        return self.energy

    def __abs__(self):
        return self.health + self.energy

    def __call__(self):
        """ Turn the object into a function. I can call the object
        using object() """
        print('The monster was called.')

    def __add__(self, other):
        """ Add something to my object, treating it as a number """
        return self.health + other

    def __str__(self):
        return f'A monster with health {self.health} and energy {self.energy}'

    # Methods
    def present(self):
        print(f"This object has {self.health} health and {self.energy} energy.")


monster1 = Monster(10, 20)
monster2 = Monster(energy=100, health=50)

# ATTRIBUTES
print(monster1.health, monster2.health)

# METHODS
monster1.present()
monster2.present()

# DUNDER METHODS
print(len(monster1))

print(abs(monster2))

monster1()

print(monster1 + 55)

print(str(monster2))
print(monster2)  # same result because print() is trying to find a string

# DEFAULT DUNDER METHODS
# To get all the dunder methods, the attributes and the normal
# methods of an object, I can use the dir() function.
# I can see the dunder methods present in the object by default and the ones I
# created in my code.
print(dir(monster1))

# To get all the attributes of the object in a dictionary
print(monster2.__dict__)
print(vars(monster2))
