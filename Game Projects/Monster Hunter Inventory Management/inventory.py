# Inventory Class and Weapon Class

# Inventory class methods - Add weapon, replace weapon (upgrade), print inventory
# Weapon Class methods - weapon type, damage, element, element damage, affinity

# Add function to organize weapons by their type within the inventory class
from weapon import Weapon

class Inventory:
    def __init__(self):
        self.stash = []
        self.file_path = r"C:\Users\Westin\Downloads\Programming Languages\Python\Portfolio\Projects\Misc Projects\Monster Hunter Inventory Management\user_inventory.txt"
    
    # Method adds newly crafted weapons to inventory
    def add_weapon(self, weapon):
        self.stash.append(weapon)
        self.save_inventory()
        
    # Method replaces the desired weapon with the upgraded version 
    def upgrade_weapon(self, new_weapon, old_weapon):
        for i, item in enumerate(self.stash):
            if item == old_weapon:
                self.stash[i] = new_weapon
                self.save_inventory()
                return
            
        print("That is not in your inventory!")
        
    def print_stash(self):
        if len(self.stash) == 0:
            print("You are carrying nothing.")
            
        else:
            print("Your Inventory:")
            for weapon in self.stash:
                print(f"- {weapon.name} {weapon.type} {weapon.element}")
                print(f"Damage: {weapon.damage}")
                print(f"Element Damage: {weapon.element_damage}")
                print(f"Affinity: {weapon.affinity}")

    def save_inventory(self):
        with open(self.file_path, "w") as file:
            file.write("Name, Weapon Type, Damage, Affinity, Element, Element Damage\n")  # Field labels
            for weapon in self.stash:
                file.write(f"{weapon.name}, {weapon.type}, {weapon.damage}, {weapon.affinity}, {weapon.element}, {weapon.element_damage}\n")

    def load_inventory(self):
        try:
            with open(self.file_path, "r") as file:
                lines = file.readlines()
                if len(lines) > 1:
                    field_labels = lines[0].strip().split(",")
                    for line in lines[1:]:
                        weapon_data = line.strip().split(",")
                        if len(weapon_data) == len(field_labels):
                            weapon = dict(zip(field_labels, weapon_data))
                            weapon_obj = Weapon(weapon['Name'], weapon['Weapon Type'], weapon['Damage'],
                                                weapon['Affinity'], weapon['Element'], weapon['Element Damage'])
                            self.stash.append(weapon_obj)

        except FileNotFoundError:
            print(f"Inventory file '{self.file_path}' not found. Starting with an empty inventory.")
    
    def clear_inventory(self):
        user_input = input("Are you sure you want to clear your inventory? [yes] [no]").lower()
        while True:
            if user_input == "yes":
                with open(self.file_path, "w") as file:
                    file.truncate(0)
                print("File cleared successfully.")
                
            elif user_input == "no":
                return False