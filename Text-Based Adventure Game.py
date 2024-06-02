# Importing necessary modules
import random

# Game constants
WIDTH, HEIGHT = 80, 20
PLAYER_HEALTH = 100
MONSTER_HEALTH = 50

# Game classes
class Player:
    def __init__(self, name):
        self.name = name
        self.health = PLAYER_HEALTH
        self.inventory = []

    def attack(self, monster):
        damage = random.randint(10, 20)
        monster.health -= damage
        print(f"You attack the {monster.name} for {damage} damage!")

    def use_item(self, item):
        if item in self.inventory:
            if item == "healing_potion":
                self.health += 20
                print("You drink a healing potion and regain 20 health!")
            elif item == "sword":
                print("You equip the sword and deal more damage!")
            self.inventory.remove(item)

class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, player):
        damage = random.randint(10, 20)
        player.health -= damage
        print(f"The {self.name} attacks you for {damage} damage!")

class Room:
    def __init__(self, description, items, monsters):
        self.description = description
        self.items = items
        self.monsters = monsters

# Game rooms
rooms = [
    Room("You are in a dark forest.", ["healing_potion"], [Monster("Goblin", MONSTER_HEALTH)]),
    Room("You are in a cave.", ["sword"], [Monster("Troll", MONSTER_HEALTH * 2)]),
    Room("You are in a castle.", [], [Monster("Dragon", MONSTER_HEALTH * 5)]),
]

# Game logic
def game_loop(player):
    current_room = 0
    while True:
        print(rooms[current_room].description)
        print("You have the following items:")
        for item in player.inventory:
            print(item)
        print("You see the following monsters:")
        for monster in rooms[current_room].monsters:
            print(monster.name)
        action = input("What do you do? (move, attack, use item) ")
        if action == "move":
            current_room = (current_room + 1) % len(rooms)
        elif action == "attack":
            monster = random.choice(rooms[current_room].monsters)
            player.attack(monster)
            if monster.health <= 0:
                rooms[current_room].monsters.remove(monster)
                print(f"You killed the {monster.name}!")
        elif action == "use item":
            item = input("Which item do you want to use? ")
            player.use_item(item)

# Game start
player_name = input("What is your name? ")
player = Player(player_name)
game_loop(player)