import time
import sys 
import os

class Player:
    def __init__(self, current_room, health = 100):
        self.current_room = current_room
        self.inventory = [axe]
        self.equipped = fists
        self.health = health
    # Method that moves the player around the map depending on the current rooms exits
    def move(self, direction):
        if self.current_room.exits[direction] is None:
            print(f"There is no room {direction} of here.\n")
        else:
            self.current_room = self.current_room.exits[direction]
            print(f"You move to the {self.current_room.name}.")
            print(self.current_room.description)
        
        if len(player.current_room.enemies_in_room) > 0:
            enemy = player.current_room.enemies_in_room[0]  # Assuming only one enemy per room for now
            combat = Combat(player, enemy)
            combat.start()

    # Method that prints the player's inventory
    def print_inventory(self):
        objects_in_inventory = self.inventory
        if len(objects_in_inventory) == 0:
            print("You are carrying nothing.")
        else:
            print("Your inventory:")
            for items in self.inventory:
                print(f"- {items.name}")
    # Method that picks up items from the room and adds them to the player's inventory
    def pick_up_object(self, item_name):
        room = self.current_room
        found_item = False
        for r_item in room.contents:
            if r_item.name == item_name:
                item = r_item
                self.inventory.append(item)
                room.contents.remove(item)
                print(f"You picked up the {item.name}")
                found_item = True
        if not found_item:
            print("That item is not in the room.")
    # Method that equips a weapon from the player's inventory
    def equip_object(self, item_name):
        if self.equipped != fists:
            self.inventory.append(self.equipped)
        found_item = False    
        for r_item in self.inventory:
            if r_item.name == item_name:
                self.equipped = r_item
                self.inventory.remove(r_item)
                print(f"You equipped the {r_item.name}")
                found_item = True
        if not found_item:
            print("You don't have that in your inventory.")
    # Method that drops an item from the player's inventory
    def drop_object(self, item_name):
        found_item = False    
        for r_item in self.inventory:
            if r_item.name == item_name:
                self.inventory.remove(r_item)
                print(f"You dropped the {r_item.name}")
                found_item = True
        if not found_item:
            print("You don't have that in your inventory.")
    # Method that prints the weapon that is held in their hand
    def print_equipped(self):
        if self.equipped != fists:
            print(f"You hold an {self.equipped.name} in your hand.")
        else:
            print("You are holding nothing.")
    
    def player_attack(self, enemy):
        damage = self.equipped.damage
        enemy.health -= damage
        print(f"You struck the {enemy.name} for {damage} damage.")
        print(" ")

class Enemies:
    def __init__(self, name, description, health, weapon):
        self.name = name
        self.description = description
        self.health = health
        self.weapon = weapon
        self.encounter_dialogue = ""

    def enemy_attack(self, player):
        damage = self.weapon.damage
        player.health -= damage
        print(f"{self.name} struck you for {damage} damage")
        print(" ")
        print(f"You have {player.health} health left.")

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Weapon(Item):
    def __init__(self, name, description, damage):
        super().__init__(name, description)
        self.damage = damage

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {"north": None, "east": None, "south": None, "west": None}
        self.contents = []
        self.enemies_in_room = []

class Combat:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
    
    def start(self):
        slow_print(self.enemy.encounter_dialogue)
        print(f"You are now in combat with {self.enemy.name}")
        while self.player.health > 0 and self.enemy.health > 0:
            time.sleep(1)
            combat_command = input("| Attack | Inventory | Equip |").lower()
            os.system('cls')
            if combat_command == "attack":
                self.player.player_attack(self.enemy)
                
            elif combat_command == "inventory":
                self.player.print_inventory()
                
            elif combat_command == "equip":
                self.player.equip_object(self.player.item_name)
                
            if self.enemy.health > 0:
                self.enemy.enemy_attack(self.player)
                
        if self.player.health > 0:
            print(f"You have defeated the {self.enemy.name}")
            
        else:
            print(f"You have been defeated by the {self.enemy.name}")
            return False

    def remove_enemy(self, enemy):
        self.player.current_room.enemies_in_room.remove(enemy)



sword = Weapon("sword", "A sword", 5)
rusty_dagger = Weapon("rusty dagger", "An iron dagger that is covered in rust.", 2)
axe = Weapon("axe", "A steel axe with a chipped blade.", 10) 
rapier = Weapon("rapier", "A sword", 5)
fists = Weapon("fists", "Your fists.", 1)
bite = Weapon(" ", " ", 5)
possible_weapons = {"rusty dagger": rusty_dagger, "axe": axe}

orc_1 = Enemies("Drutha The Orc", "A rotund green orc wielding an axe.", 50, axe)
orc_1.encounter_dialogue = "Inside the guard room stands an orc wielding a battered iron axe covered in dried blood."

wolf_1 = Enemies("Wolf.","A large diseased white wolf with mangled hair.", 30, bite)

guard_room = Room("Guard station.", "Guard station." )
guard_room.enemies_in_room = [orc_1]

cave_start = Room("Cave", "A dark and tenebrous cave.")
cave_start.contents = [rapier]
cave_start.exits["north"] = guard_room

player = Player(cave_start, 100)



       
def slow_print(input_str):
    for c in input_str:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.005)
    sys.stdout.write('\n')