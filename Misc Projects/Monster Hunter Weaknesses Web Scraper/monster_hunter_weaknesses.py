import requests
from bs4 import BeautifulSoup
import os

# Add ability to print out monster names

def print_monster_weakness(monster_name):
    url = "https://monsterhunterrise.wiki.fextralife.com/Monsters"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Pulls data from table in the website
    monster_table = soup.find("table", class_="wiki_table sortable searchable")

    weakness_names = ["Fire", "Water", "Thunder", "Ice", "Dragon"]

    for row in monster_table.find_all("tr"):
        columns = row.find_all("td")
        if len(columns) >= 2:
            current_monster_name = columns[0].text.strip()
            if current_monster_name.lower() == monster_name.lower():
                print("--------------------")
                print(f"Monster Name: {current_monster_name}\n")
                # Prints data with the corresponding weakness
                for weakness_name, column in zip(weakness_names, columns[1:6]):
                    monster_type = column.text.strip()
                    print(f"Monster Weakness {weakness_name}: {monster_type}")
                print("--------------------")
                break
    else:
        print("Monster not found.")

def main():
    while True:
        user_input = input("Enter the monster name or 'quit': ")
        os.system('cls')
        if user_input.lower() == 'quit':
            print("Exiting program...")
            break
        else:
            print_monster_weakness(user_input)
            print()

# Run the driver code
main()



        
