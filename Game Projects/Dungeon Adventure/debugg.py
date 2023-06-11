class Player:
    def __init__(self, current_room, health = 100):
        self.current_room = current_room
        self.inventory = Inventory(self.inventory)
        self.equipped = fists
        self.health = health
        self.actions = PlayerActions(self.actions)
        self.body_modifications = BodyModifications(self)
    

class PlayerActions:
    def __init__(self, player):
        self.player = player
    
    def move(self, direction):
        if self.player.current_room.exits[direction] is None:
            print(f"There is no room {direction} of here.\n")
        else:
            self.player.current_room = self.player.current_room.exits[direction]
            print(f"You move to the {self.player.current_room.name}\n")
            print(self.player.current_room.description)
            print(" ")
        
        if len(player.current_room.enemies_in_room) > 0:
            enemy = player.current_room.enemies_in_room[0]
            combat = Combat(player, enemy)
            combat.start()
            
    def print_equipped(self):
        if self.equipped != fists:
            
            print(f"You hold a {self.equipped.name} in your hand.")
        else:
            
            print("You are holding nothing.")
    

class BodyModifications:
    def __init__(self, player):
        self.player = player
        self.face = "Normal"
        self.hands = "Normal"
        self.feet = "Normal"
        self.genitals = "Normal"

class Inventory:
    def __init__(self, player):
        self.player = player
        self.player_inventory = []
        self.current_room = player.current_room
    
    def print_equipped(self):
        if self.equipped != fists:
            
            print(f"You hold a {self.equipped.name} in your hand.")
        else:
            
            print("You are holding nothing.")

    def pick_up_object(self, item_name):
        room = self.current_room
        found_item = False
        for r_item in room.contents:
            if r_item.name == item_name:
                item = r_item
                self.player_inventory.append(item)
                room.contents.remove(item)
                print(f"You picked up the {item.name}")
                found_item = True
        if not found_item:
            print("That item is not in the room.")

    def equip_object(self, item_name):
        if self.equipped != fists:
            self.player_inventory.append(self.equipped)
        found_item = False    
        for r_item in self.player_inventory:
            if r_item.name == item_name:
                self.equipped = r_item
                self.player_inventory.remove(r_item)
                print(f"You equipped the {r_item.name}")
                found_item = True
        if not found_item:
            print("You don't have that in your inventory.")
    
    def print_inventory(self):
        objects_in_inventory = self.player_inventory
        if len(objects_in_inventory) == 0:
            print("You are carrying nothing.")
        else:
            print("Your inventory:")
            for items in self.player_inventory:
                print(f"- {items.name}")
     
    def drop_object(self, item_name):
        found_item = False    
        for r_item in self.player_inventory:
            if r_item.name == item_name:
                self.player_inventory.remove(r_item)
                print(f"You dropped the {r_item.name}")
                found_item = True
        if not found_item:
            print("You don't have that in your inventory.")
            
class Combat:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
    
    def player_attack(self, enemy):
        damage = self.equipped.damage
        enemy.health -= damage
        print(f"You struck the {enemy.name} for {damage} damage.")
        print(" ")
    
    def enemy_attack(self, player):
        damage = self.weapon.damage
        player.health -= damage
        print(f"{self.name} struck you for {damage} damage")
        print(" ")
        print(f"You have {player.health} health left.")
    
    def remove_enemy(self, enemy):
        self.player.current_room.enemies_in_room.remove(enemy)
    
    def start(self):
        print(self.enemy.encounter_dialogue)
        print(f"You are now in combat with {self.enemy.name}")
        while self.player.health > 0 and self.enemy.health > 0:
            
            combat_command = input("| Attack | Inventory | Equip |").split()
            
            if combat_command[0] == "attack":
                self.player.player_attack(self.enemy)
                
            elif combat_command[0] == "inventory":
                self.player.print_inventory()
                
            elif combat_command[0] == "equip":
                item_name = ''.join(combat_command[1:])
                self.player.equip_object(item_name)
        
            else:
                print("Invalid input.")
                
            if self.enemy.health > 0:
                self.enemy.enemy_attack(self.player)
                
        if self.player.health > 0:
            print(f"You have defeated the {self.enemy.name}")
            self.remove_enemy(self.enemy)
            
            
        else:
            print(f"You have been defeated by the {self.enemy.name}")
            return False

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

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {"north": None, "east": None, "south": None, "west": None}
        self.contents = []
        self.enemies_in_room = []

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Weapon(Item):
    def __init__(self, name, description, damage):
        super().__init__(name, description)
        self.damage = damage

class Potion(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.effect_description = None
        self.effect = None

sword = Weapon("sword", "A sword", 5)
rusty_dagger = Weapon("rusty dagger", "An iron dagger that is covered in rust.", 2)
axe = Weapon("axe", "A steel axe with a chipped blade.", 10) 
rapier = Weapon("rapier", "A sword", 5)
fists = Weapon("fists", "Your fists.", 1)
bite = Weapon(" ", " ", 5)

orc_1 = Enemies("Drutha The Orc", "A rotund green orc wielding an axe.", 10, axe)
orc_1.encounter_dialogue = "Inside the guard room stands an orc wielding a battered iron axe covered in dried blood."

wolf_1 = Enemies("Wolf.","A large diseased white wolf with mangled hair.", 30, bite)

guard_room = Room("Guard station.", "Guard station." )
guard_room.enemies_in_room = [orc_1]

cave_start = Room("Cave", "A dark and tenebrous cave.")
cave_start.contents = [rusty_dagger, axe]
cave_start.exits["north"] = guard_room

guard_room.exits["south"] = cave_start

player = Player(cave_start, 100)