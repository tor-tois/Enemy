from enemy import *

class Squirtle(Enemy):
    def __init__(self, health, attack):
        super().__init__(type_of_enemy="Squirtle", health=health, attack=attack)

    def talk(self):
        print(f"Squirtle.....!")
    def category(self):
        print(f"{self._Enemy__type_of_enemy} is a Water type Pokemon")