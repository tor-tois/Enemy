from enemy import *
from pikachu import *
from squirtle import *
import random

def battle(e1: Enemy, e2: Enemy):
    e1.talk()
    e2.talk()

    while e1.health > 0 and e2.health > 0:
        print("------------------")
        # Special attacks for both enemies & conditions
        if e1.health < e1.max_health * 0.5:
            e1.special_attack()
            print("------------------")
        if e2.health < e2.max_health * 0.5:
            e2.special_attack()
            print("------------------")

        # Randomly select which enemy attacks first
        attacker, defender = random.sample((e1, e2), 2)

        print(f"{attacker.get_enemy()} attacks first!")

        # first attack
        defender.health -= attacker.attack
        attacker.attack_enemy()

        if defender.health < 0:
            defender.health = 0
        print(f"{defender.get_enemy()} : {defender.health} HP left")

        # check if the defender 
        if defender.health <= 0:
            break

        # conter attack
        attacker.health -= defender.attack
        defender.attack_enemy()

        if attacker.health < 0:
            attacker.health = 0
        print(f"{attacker.get_enemy()} : {attacker.health} HP left")

    print("------------------")

    if e1.health > 0:
        print(f"{e1.get_enemy()} wins!")
    else:
        print(f"{e2.get_enemy()} wins!")


pikachu = Pikachu(90, 67)
squirtle = Squirtle(79, 56)


battle(pikachu, squirtle)