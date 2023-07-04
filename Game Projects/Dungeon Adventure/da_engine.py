from da_items import *
from da_rooms import Room
from da_enemies import Enemies
import time
import sys 
import os

# Class that takes the inputs from main() to initiate the player's desired actions
class Player:
    def __init__(self, current_room, health = 100):
        self.current_room = current_room
        self.inventory = [axe, health_potion]
        self.equipped = fists
        self.health = health
        
    def move(self, direction):
        # Check to see if the current room has an exit in the direction that is inputted
        if self.current_room.exits[direction] is None:
            print(f"There is no room {direction} of here.\n")
        else:
            self.current_room = self.current_room.exits[direction]
            print(f"You move to the {self.current_room.name}\n")
            slow_print(self.current_room.description)
            print(" ")
            
        # If there is an enemy in the room that is moved into, the program will initiate combat
        if len(player.current_room.enemies_in_room) > 0:
            enemy = player.current_room.enemies_in_room[0]  # Assuming only one enemy per room for now
            combat = Combat(player, enemy)
            combat.start()

    def print_inventory(self):
        objects_in_inventory = self.inventory
        if len(objects_in_inventory) == 0:
            print("You are carrying nothing.")
        else:
            print("Your inventory:")
            for inv_items in self.inventory:
                print(f"- {inv_items.name}")
                
    def pick_up_object(self, item_name):
        # Checks to see if the item the player inputs is in the current room
        # If it is, then the item is removed from the room's "inventory" and added to the player's 
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
            
    def equip_object(self, item_name):
        # If there is a weapon that is already equipped, it is moved into the player's inventory
        # before the desired weapon is equipped. Also, prevents "fists" from being added to the inventory
        if self.equipped != fists:
            self.inventory.append(self.equipped)
        found_item = False    
        for inv_item in self.inventory:
            if inv_item.name == item_name:
                self.equipped = inv_item
                self.inventory.remove(inv_item)
                print(f"You equipped the {inv_item.name}")
                found_item = True
        if not found_item:
            print("You don't have that in your inventory.")
            
    def drop_object(self, item_name):
        # Checks for the item inputted inside the player's inventory
        # If it is in the player's inventory, then it is deleted
        found_item = False
        for inv_item in self.inventory:
            if inv_item.name == item_name:
                self.inventory.remove(inv_item)
                print(f"You dropped the {inv_item.name}")
                found_item = True
        if not found_item:
            print("You don't have that in your inventory.")
            
    def print_equipped(self):
        if self.equipped != fists:
            os.system('cls')
            print(f"You hold a {self.equipped.name} in your hand.")
        else:
            os.system('cls')
            print("You are holding nothing.")
    
    def use(self, item_name):
        found_item = False
        for inv_item in self.inventory:
            if inv_item.name == item_name and isinstance(inv_item, HealingPotion):
                self.health += inv_item.effect["amount"]
                print(f"You gained {inv_item.effect['amount']}. Health: {self.health}")
                found_item = True
        if not found_item:
            print("You don't have that in your inventory.")
        
               
class Combat:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
    
    def player_attack(self):
        damage = self.player.equipped.damage
        self.enemy.health -= damage
        print(f"You struck the {self.enemy.name} for {damage} damage.")
        print(" ")
    
    def enemy_attack(self, player):
        damage = self.enemy.equipped.damage
        player.health -= damage
        print(f"{self.enemy.name} struck you for {damage} damage")
        print(" ")
        print(f"You have {player.health} health left.")  
        
    # Removes enemy from the room when defeated so that the player doesn't have to 
    # fight it again when moving back and forth between rooms. Also drops the enemies' items
    # for the player to pick up
    def remove_enemy(self, enemy):
        if len(enemy.contents) != 0:
            print(f"{enemy.name} dropped: ")
            for item in enemy.contents:
                player.current_room.contents.append(item)
                print(f"- {item.name}.")
        self.player.current_room.enemies_in_room.remove(enemy)
        
    def start(self):
        slow_print(self.enemy.encounter_dialogue)
        print(f"You are now in combat with {self.enemy.name}")
        while self.player.health > 0 and self.enemy.health > 0:
            # Used so the player can check inventory and equip items without giving up a turn
            # The enemy only gets a turn once the player attacks (sets enemy_turn to true)
            enemy_turn = False
            time.sleep(1)
            combat_command = input("| Attack | Inventory | Equip |").split()
            os.system('cls')
            if combat_command[0] == "attack":
                self.player_attack()
                enemy_turn = True
                
            elif combat_command[0] == "inventory":
                self.player.print_inventory()
                
            elif combat_command[0] == "equip":
                item_name = ''.join(combat_command[1:])
                self.player.equip_object(item_name)
                
            else:
                print("Invalid input.")
                
            if self.enemy.health > 0 and enemy_turn == True:
                self.enemy_attack(self.player)
                
        if self.player.health > 0:
            print(f"You have defeated the {self.enemy.name}")
            self.remove_enemy(self.enemy)
            
            
        else:
            print(f"You have been defeated by the {self.enemy.name}")
            return False
        



sword = Weapon("sword", "A sword", 5)
rusty_dagger = Weapon("rusty dagger", "An iron dagger that is covered in rust.", 2)
axe = Weapon("axe", "A steel axe with a chipped blade.", 10) 
rapier = Weapon("rapier", "A sword", 5)
fists = Weapon("fists", "Your fists.", 1)
possible_weapons = {"rusty dagger": rusty_dagger, "axe": axe, "rapier": rapier, "sword": sword}

bite = Weapon(" ", " ", 5)

orc_1 = Enemies("Drutha The Orc", "A rotund green orc wielding an axe.", 20, axe)
orc_1.encounter_dialogue = "Inside the guard room stands an orc wielding a battered iron axe covered in dried blood."
orc_1.contents = [rapier, rusty_dagger]

wolf_1 = Enemies("Wolf.","A large diseased white wolf with mangled hair.", 30, bite)

guard_room = Room("Guard station.", "Guard station." )
guard_room.enemies_in_room = [orc_1]

cave_start = Room("Cave", "A dark and tenebrous cave.")
cave_start.contents = [rusty_dagger, axe]
cave_start.exits["north"] = guard_room

guard_room.exits["south"] = cave_start

health_potion = HealingPotion("health potion", "A giga healing potion", 5)

player = Player(cave_start, 100)



# Makes the text scroll like an rpg
def slow_print(input_str):
    for c in input_str:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.005)
    sys.stdout.write('\n')
