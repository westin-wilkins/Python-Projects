from da_engine import *

import time
import sys 
import os
        
# Function that runs the game and takes the players inputs
def main():
    
    slow_print("""\nYou wake up to the sound of water striking the stone floor
that you're laying on. You get up and rub at your eyes to find yourself
inside of a dark cave. Torch light pours out from a room north of you,
illuminating a rusty dagger on the floor.\n""")
    
    print("What do you do?")
    
    while True:
        allowed_commands = ["move", "inventory", "pick", "equip", "drop", "examine", "equipped", "quit"]
        
        command = input("\n| Move [Cardinal Direction] | Inventory | Pick Up [Item] | Equip [Item]" \
                           "| Drop [Item] | Examine Room | Equipped Weapon | Quit | \n ").lower().split()
        if command[0] in allowed_commands:
            if command[0] == "quit":
                os.system('cls')
                print("\nThanks for playing!")
                return False
            else:
                player_actions(command)
        else:
            
            invalid_input()


# Put all possible actions within player_actions to reduce complexity of main()
def player_actions(command):
    if command[0] == "move":
        handle_movement(command)
        
    elif command[0] == "inventory":
        handle_inventory()
    
    elif command[0] == "pick":
        handle_pick_up(command)
        
    elif command[0] == "equip":
        handle_equip(command)
            
    elif command[0] == "drop":
        handle_drop(command)
            
    elif command[0] == "examine":
        handle_examine(command)
            
    elif command[0] == "equipped":
        player.print_equipped()
    
# Function that makes the text scroll like an rpg
def slow_print(input_str):
    for c in input_str:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.005)
    sys.stdout.write('\n')


def invalid_input():
    print("Not a valid input.")

def handle_movement(command):
    if len(command) > 1:
        direction = command[1]
        if direction in ["north", "east", "south", "west"]:
            # Clears player's input from the screen for a cleaner look
            os.system('cls')
            player.move(direction)
        
    else:
        os.system('cls')
        invalid_input()
        
def handle_inventory():
    os.system('cls')
    player.print_inventory()

def handle_pick_up(command):
    if len(command) > 2:
        item = " ".join(command[2:])
        os.system('cls')
        player.pick_up_object(item)
        
    else:
        os.system('cls')
        invalid_input()
        
        
def handle_equip(command):
    if len(command) > 1:
        item = " ".join(command[1:])
        os.system('cls')
        player.equip_object(item)
        
    else:
        os.system('cls')
        invalid_input()
        
def handle_drop(command):
    if len(command) > 1:
        item = "_".join(command[1:])
        os.system('cls')
        player.inventory.drop_object(item)
    else:
        os.system('cls')
        invalid_input()
    
def handle_examine(command):
    if len(command) > 1:
        if command[1] == "room":
            os.system('cls')
            print(player.current_room.description)
                    
        elif command[1].name in player.inventory:
            os.system('cls')
            print("This is were the description of the item goes.")
        
        else:
            os.system('cls')
            invalid_input()
            
    else:
        os.system('cls')
        invalid_input()
        
if __name__ == '__main__':
    main()