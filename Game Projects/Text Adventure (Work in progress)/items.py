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


        
rusty_dagger = Weapon("Rusty Dagger", "An iron dagger that is covered in rust.", 2)
axe = Weapon("Axe", "A steel axe with a chipped blade.", 10) 
rapier = Weapon("Rapier", "A sword", 5)
fists = Weapon("Fists", "Your fists.", 1)
bite = Weapon("","", 5)
claws = Weapon("", "", 3)
list_of_weapons = [rusty_dagger, axe, rapier, fists, bite, claws]