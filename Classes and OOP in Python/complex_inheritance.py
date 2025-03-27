# MRO is the "Method resolution order", indicates in what order the
# parent __init__() methods are begin called. ClassName.mro()
# it derives from the order of the arguments passed after the
# creation of a child class:
#   class Something(first_argument, second_argument...)

# The first time we call super(), we are referring to the first argument.


class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    def attack(self, amount):
        print(f"{amount} damage was dealt!")

    def move(self, speed):
        print(f"The monster moves at a speed of {speed}")


class Fish:
    def __init__(self, speed, has_scales):
        self.speed = speed
        self.has_scales = has_scales

    def swim(self):
        print(f"The fish is swimming at a speed of {self.speed}")


class Shark(Monster, Fish):
    def __init__(self, bite_strength, health, energy):
        self.bite_strength = bite_strength

        Monster.__init__(self, health, energy)


print(Shark.mro())

shark = Shark(50, 200, 55,)

print(shark.speed)
