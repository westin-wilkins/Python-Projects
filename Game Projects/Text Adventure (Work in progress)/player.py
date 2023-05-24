import items
class Player:
    def __init__(self, name, starting_room, health = 100):
        self.name = name
        self.starting_room = starting_room
        self.inventory = []
        self.equipped = fists
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


