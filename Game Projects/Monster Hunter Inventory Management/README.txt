# Inventory Management System For Monster Hunter Rise

This is a simple inventory management system that allows users to add and upgrade weapons in their inventory. The inventory data is stored in a text file.

## Features

- Add weapons to the inventory with or without an element.
- Upgrade weapons in the inventory. 
- Save the inventory data to a text file.
- Load the inventory data from a text file.

## Requirements

- Python 3.x

## Usage

1. Clone the repository or download the source code files.

2. Run the `main.py` file to start the program.

    ```shell
    python main.py
    ```

3. The program will prompt you with options:

    - `add`: Add a weapon to the inventory.
    - `upgrade`: Upgrade a weapon in the inventory.
    - `quit`: Exit the program.

4. When adding a weapon, the program will ask for weapon details like name, type, damage, etc. Follow the prompts to add the weapon to the inventory.

5. When upgrading a weapon, the program will ask for the name of the weapon to be upgraded and the name of the upgraded weapon. If both weapons are found in the inventory, the upgrade will be performed.

6. The inventory data is automatically saved to a text file named `inventory.txt` in the same directory as the program. If the file doesn't exist, it will be created.

## File Structure

- `main.py`: The main entry point of the program.
- `inventory.py`: Contains the `Inventory` class responsible for managing the inventory and file I/O operations.
- `weapon.py`: [Optional] Contains the `Weapon` class (currently unused) for representing weapon objects.
- `README.md`: This file.
