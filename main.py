from enemy import *

zombie = Enemy("Zombie", 10, 1)


print(f"{zombie.type_of_enemy} has {zombie.health} health and {zombie.attack} attack power.")
print(zombie.talk())
print(zombie.move_forward())
print(zombie.attack_enemy())