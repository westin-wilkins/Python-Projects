import os
from inventory import Inventory
from weapon import Weapon

def main():
    inventory = Inventory()
    while True:
        command = input("What would you like to do? [add, upgrade, quit]\n").lower()
        if command == "add":
            clear_screen()
            add_weapon_command(inventory)

        elif command == "upgrade":
            clear_screen()
            upgrade_weapon(inventory)
            
        elif command == "clear":
            clear_screen()

        elif command == "quit":
            clear_screen()
            print("Exiting program...")
            return False

        else:
            clear_screen()
            print("That is not a valid input!\n")


def add_weapon_command(inventory):
    print("If the weapon does not have an element input none for element and 0 for element damage.")
    weapon_stats = input("[Name] [Weapon Type] [Damage] [Affinity] [Element] [Element Damage]\n").lower().split()
    
    stat_value_check_add_weapon(weapon_stats, inventory)

def upgrade_weapon(inventory):
    print("If the weapon does not have an element input none for element and 0 for element damage.")
    new_weapon_stats = input("[Name] [Weapon Type] [Damage] [Affinity] [Element] [Element Damage]\n").lower().split()
    old_weapon_name = input("Enter the name of the weapon to be upgraded:\n")

    for weapon in inventory.stash:
        if weapon.name == old_weapon_name:
            old_weapon = weapon

    if old_weapon:
        stat_value_check_upgrade_weapon(new_weapon_stats, old_weapon)
        
    else:
        print("One or both of the weapons were not found in the inventory.")
        
        
def stat_value_check_add_weapon(weapon_stats, inventory):
    if len(weapon_stats) == 6 and weapon_stats[2].isdigit() and weapon_stats[3].isdigit() and weapon_stats[5].isdigit():
        weapon = Weapon(weapon_stats[0], weapon_stats[1], weapon_stats[2], weapon_stats[3],
                        weapon_stats[4], weapon_stats[5])
        inventory.add_weapon(weapon)
        clear_screen()
        
    else:
        print("Invalid input!")

def stat_value_check_upgrade_weapon(weapon_stats, inventory):
    if len(weapon_stats) == 6 and weapon_stats[2].isdigit() and weapon_stats[3].isdigit() and weapon_stats[5].isdigit():
        weapon = Weapon(weapon_stats[0], weapon_stats[1], weapon_stats[2], weapon_stats[3],
                        weapon_stats[4], weapon_stats[5])
        inventory.add_weapon(weapon)
        clear_screen()


def clear_screen():
    os.system("cls")

if __name__ == "__main__":
    main()