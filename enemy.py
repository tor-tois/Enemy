class Enemy:
    
    # Constructor method to initialize the attributes of the Enemy class
    def __init__(self, type_of_enemy, health, attack):
        self.__type_of_enemy = type_of_enemy
        self.health = health
        self.max_health = health
        self.attack = attack
    # Encapsulation: Getter method to access the private attribute __type_of_enemy
    def get_enemy(self):
        return self.__type_of_enemy

    # abstract methods that will be implemented by subclasses
    def talk(self):
        print(f"I am a {self.__type_of_enemy}")

    def move_forward(self):
        print(f"{self.__type_of_enemy} closer to you")

    def attack_enemy(self):
        print(f"{self.__type_of_enemy} attack for {self.attack} damage")

    def special_attack(self):
        print(f"Enemy has no special attack")