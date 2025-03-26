class Monster:
    def __init__(self, func):
        self.func = func


class Attacks:

    def bite(self):
        print("Bite!")

    def strike(self):
        print("Strike!")

    def slash(self):
        print("Slash!")

    def kick(self):
        print("Kick!")


# FIRST METHOD
# create an instance of the Attacks class
attacks = Attacks()
monster = Monster(attacks.kick)
monster.func()

# SECOND METHOD
# turn the Attacks class into an object by calling it: Attacks()
monster = Monster(Attacks().slash)

monster.func()
