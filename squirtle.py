from enemy import Enemy
import random

class Squirtle(Enemy):
    def __init__(self, health, attack):
        super().__init__(type_of_enemy="Squirtle", health=health, attack=attack)

    def special_attack(self):
            if random.random() < 0.3:
                    self.health += 8
                    print(f"{self.get_enemy()} uses Water Pulse "
                          f"and gains 8 health")
            else: 
                print(f"{self.get_enemy()} uses Water Pulse but it failed")

    def talk(self):
        print(f"Squirtle.....!")

    def category(self):
        print(f"{self._Enemy__type_of_enemy} is a Water type Pokemon")