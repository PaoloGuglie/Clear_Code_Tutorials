class Monster:

    # Attributes
    health = 50
    energy = 100

    # Methods
    def attack(self, amount):
        print("The monster has attacked!")
        print(f"{amount} damage was dealt.")
        self.energy -= 20

    def move(self, speed):
        print("The monster has moved")
        print(f"It has a speed of {speed}")


class Shark(Monster):
    """ With simple inheritance, I only need to
    call the parent's class name at the top """

    def __init__(self, speed):
        """ __init__() only used to set a new attribute """

        self.speed = speed

    def bite(self):
        print("The shark has bitten!")

    def move(self):
        """ This method overrides a parent's class method """
        print("The shark has moved")
        print(f"It has a speed of {self.speed}")


shark = Shark(5)

print(shark.health, shark.speed)
shark.attack(300)
print(shark.energy)
shark.move()

print("---------------------")
################################################

# More complex inheritance:


class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    def attack(self, amount):
        print("The monster has attacked!")
        print(f"{amount} damage was dealt.")
        self.energy -= 20

    def move(self, speed):
        print("The monster has moved")
        print(f"It has a speed of {speed}")


# I have to call the parent's __init__() method:

# Old method:
class Shark(Monster):
    def __init__(self, speed, health, energy):
        Monster.__init__(self, health, energy)
        self.speed = speed


shark = Shark(120, 100, 80)


# New method:
class Shark(Monster):
    def __init__(self, speed, health, energy):
        """ The super() function gets the parent class, so I can call
         the __init__() method of that class as well.
          Better for multiple / more complex inheritance """

        super().__init__(health, energy)

        self.speed = speed


shark = Shark(120, 100, 80)


# I can also do:
class Shark(Monster):
    def __init__(self, speed, health, energy):
        super().__init__(health, energy)

        # I can call methods from the parent class.
        # Now, when I create an object, the method is run.
        super().move(speed)


Shark(100, 1, 1)


###############################################################
print("----------------------")


class Scorpion(Monster):
    def __init__(self, poison_damage, scorpion_health, scorpion_energy):
        super().__init__(health=scorpion_health, energy=scorpion_energy)

        self.poison_damage = poison_damage

    def attack(self):
        print("The scorpion has attacked!")
        print(f"{self.poison_damage} poison damage was dealt.")


scorpion = Scorpion(30, 40, 20)

scorpion.attack()
scorpion.move(12)
print(scorpion.health, scorpion.energy)

