from enemy import *
from pikachu import *
from squirtle import *

pikachu = Pikachu(35, 55)
pikachu.get_enemy()

squirtle = Squirtle(44, 48)
squirtle.get_enemy()

print(f"This is {pikachu.get_enemy()}")
pikachu.talk()
pikachu.category()
print(f"{pikachu._Enemy__type_of_enemy} has {pikachu.health} health and {pikachu.attack} attack power.")

print()

print(f"This is {squirtle.get_enemy()}")
squirtle.talk()
squirtle.category()
print(f"{squirtle._Enemy__type_of_enemy} has {squirtle.health} health and {squirtle.attack} attack power.")

