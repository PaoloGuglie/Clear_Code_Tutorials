# MRO is the "Method resolution order", indicates in what order the
# parent __init__() methods are begin called. ClassName.mro()
# it derives from the order of the arguments passed after the
# creation of a child class:
#   class Something(first_argument, second_argument...)

# The first time we call super(), we are referring to the first argument.

# I can also use multiple ParentClassName.__init__(self, ...) to inherit
# from multiple parent classes, but it's limited.

# I will see super()__init__() in most classes because it enables inheritance
# to work across multiple classes.


class Monster:
    def __init__(self, health, energy, **kwargs):
        self.health = health
        self.energy = energy

        # to reference the Fish class (the next item according to Shark)
        super().__init__(**kwargs)

    def attack(self, amount):
        print(f"{amount} damage was dealt!")

    def move(self, speed):
        print(f"The monster moves at a speed of {speed}")


class Fish:
    def __init__(self, speed, has_scales, **kwargs):
        self.speed = speed
        self.has_scales = has_scales

        # to reference any other class following the MRO
        super().__init__(**kwargs)

    def swim(self):
        print(f"The fish is swimming at a speed of {self.speed}")


class Shark(Monster, Fish):
    """ When I call the Shark class, the __init__() method of the
    Shark class is called. Python knows the first item of inheritance
    is the Monster class.

    When I call super(), I am calling the __init__()
    method of the Monster class.

    To call the __init__() method of the Fish class, I have to
    call it from the Monster class. I can use a super() in the
    __init__() method of the Monster class. It follows the
    inheritance (MRO) set by the Shark class. If I call the Monster class
    from the Shark class, it knows to look at the fish next in line.
    If I call the monster by itself, the super() does nothing.

    I add another super(), this time in the Fish class's __init__()
    method, in case there is going to be another item in the list of
    inheritance (or in the MRO) and call it.

    To get the parameters from the Shark class to the Fish class, I
    need to use "keyword unpacking": after all the parameters (in my
    example, I do this in the Monster class), I add **kwargs. Any
    argument I get after the parameters are stored in a separate
    dictionary. Python expects the arguments in the super().__init__()
    of the Shark class to be keyword arguments.
    I pass the keyword arguments in the super().__init__() of the
    Monster class.

    In real code, the Fish class's __init__() method and its super()
    would have **kwargs. """

    def __init__(self, bite_strength, health, energy, speed, has_scales):
        self.bite_strength = bite_strength

        super().__init__(
            health=health,
            energy=energy,
            speed=speed,
            has_scales=has_scales)


print(Shark.mro())
print("------------")

shark = Shark(50, 200, 55, 120, False)

print(shark.speed, shark.has_scales)
shark.swim()
