# Every method has a reference to its class. Because of that, it's really easy
# to get and change class attributes. That makes methods easier to work with than
# functions. Less use of parameters, global keyword and return statement.
# Objects can be infulenced from outside the object itself and the local scope
# of a function.


def update_health(amount):
    global health
    health += amount


health = 10

update_health(20)

print(health)


# I can improve this code with (ugly code):
class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy


def new_update_health(amount):
    """ Here, it is clear that "monster" is not a varible
    in the local scope. Python allows direct access to
     mutable global objects """
    monster.health += amount


monster = Monster(100, 50)

new_update_health(30)

print(monster.health)


# I can also do (better code):
class MonsterNew:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    def update_health(self, amount):
        self.health += amount

    def update_energy(self, amount):
        self.energy += amount


new_monster = MonsterNew(50, 100)

new_monster.update_energy(70)

print(new_monster.energy)

#######################################


class Hero:
    def __init__(self, damage, monster):
        self.damage = damage
        self.monster = monster

    def attack(self):
        self.monster.get_damage(self.damage)


class MonsterNewNew:
    def __init__(self, health):
        self.health = health

    def get_damage(self, amount):
        self.health -= amount


monster = MonsterNewNew(100)
hero = Hero(20, monster)

hero.attack()
hero.attack()

print(monster.health)
