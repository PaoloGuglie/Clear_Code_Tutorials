# @property allows me to turn methods into attributes. This comes from the
# property() function.

class Generic:
    def __init__(self):
        self.x = 10

    def get_x(self):
        """ Method to run other code while retrieving an attribute.
        Not elegant. """

        print('get x')
        return self.x


generic = Generic()

print(generic.x)

print(generic.get_x())

# If I have many instances of a class and I want to change the class itself
# instead, I need a special function called property:
#       property(getter, setter, deleter).
# I can assign it to one attribute inside my class.
# When I look at that attribute I call "getter", when I change it I call
# "setter" and when I delete it, I call "deleter".
print("-------------------")


class Generic:
    """ When I call x, I call the getter() method that returns _x.
    Outside the class, I work with x. Inside, I use _x, which
    keeps track of the value """

    def __init__(self):
        self._x = 10

    def getter(self):
        print('get x')
        return self._x

    def setter(self, value):
        print('set x')
        self._x = value

    def deleter(self):
        print('delete x')
        del self._x

    x = property(getter, setter, deleter)


generic = Generic()

print(generic.x)

generic.x = 4
print(generic.x)

del generic.x

# RECAP: When I initiate the class, I have _x. This is the variable I actually
# store values in. Then I run the x = property(...) line, that turns x in a
# property. This property has a getter, a setter and a deleter. They are
# referring to the three methods defined before the property.
# From outside the class, whenever I am accessing x, I am running one of
# the three methods. These methods influence self._x, where I actually
# store the value. Also, I can run any other code I want when accessing
# x.
print("------------------")


# A more elegant way to write this is by using property() as a decorator:

class Generic:
    """ getter(), setter() and deleter() are renamed to the name
    of the property. I removed the property() line. """

    def __init__(self):
        self._x = 10

    # getter
    @property
    def x(self):
        print('get x')
        return self._x

    # setter
    @x.setter
    def x(self, value):
        print('set x')
        self._x = value

    # deleter
    @x.deleter
    def x(self):
        print('delete x')
        del self._x


generic = Generic()

print(generic.x)

generic.x = 4
print(generic.x)
