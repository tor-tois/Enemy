from enemy import Enemy
import random

class Pikachu(Enemy):
    def __init__(self, health, attack):
        super().__init__(type_of_enemy="Pikachu", health=health, attack=attack)        

    def special_attack(self):
        if random.random() < 0.5:
            previous_health = self.health
            self.health = min(self.max_health, self.health + 10)
            healed = self.health - previous_health
            print(f"{self.get_enemy()} uses Thunderbolt "
                  f"and gains {healed} health")
        else: 
            print(f"{self.get_enemy()} uses Thunderbolt but it failed")

    def talk(self):
        print(f"Pika Pika!")
        
    def category(self):
        print(f"{self._Enemy__type_of_enemy} is an Electric type Pokemon")