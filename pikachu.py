from enemy import *

class Pikachu(Enemy):
    def __init__(self, health, attack):
        super().__init__(type_of_enemy="Pikachu", health=health, attack=attack)

    def talk(self):
        print(f"Pika Pika!")
    def category(self):
        print(f"{self._Enemy__type_of_enemy} is an Electric type Pokemon")