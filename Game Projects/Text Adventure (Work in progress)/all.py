class Player:
    def __init__(self, name, starting_room, health = 100):
        self.name = name
        self.starting_room = starting_room
        self.inventory = []
        self.equipped = None
        self.health = health

    def take_item(self, *args):
        for item in args:
            self.inventory.append(item)
        return self.inventory
    
    def equip_item(self, item):
        for item in self.inventory:
            if item in list_of_weapons:
                self.equipped = item
                return self.equipped
            else:
                print("You can't use that as a weapon.")
    
    def print_inventory(self):
        print(f"{self.name}'s inventory:")
        for item in self.inventory:
            print(f"- {item}")
    
    def print_equipped(self):
        if self.equipped != fists:
            print(f"You hold a {self.equipped} in your hands.")
        else:
            print("You are holding nothing.")
    


        
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self):
        return (f" Debug: {self.name}  '{self.description}'")

class Weapon(Item):
    def __init__(self, name, description, damage):
        super().__init__(name, description)
        self.damage = damage

class Room:
    def __init__(self, name):
        self.name = name
        
rusty_dagger = Weapon("Rusty Dagger", "An iron dagger that is covered in rust.", 2)
axe = Weapon("Axe", "A steel axe with a chipped blade.", 10) 
rapier = Weapon("Rapier", "A sword", 5)
fists = Weapon("Fists", "Your fists.", 1)
list_of_weapons = [rusty_dagger, axe, rapier, fists]

starting_room = Room("Starting Room")
player = Player("Steve", "Starting Room")


player.take_item(fists)
player.print_inventory()
player.equip_item(fists)
player.print_equipped()