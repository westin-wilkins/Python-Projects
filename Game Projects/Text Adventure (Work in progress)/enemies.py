import items
from items import bite, claws, axe

class Enemies:
    def __init__(self, name, description, health):
        self.name = name
        self.descirption = description
        self.health = health

class Orc(Enemies):
    def __init__(self, name, description, health, weapon):
        super().__init__(name, description, health)
        self.weapon = weapon

class Wolf(Enemies):
    def __init__(self, name, description, health, weapon):
        super().__init__(name, description, health)
        self.weapon = weapon
orc_1 = Orc("Trogdor", "A rotund green orc wielding an axe.", 50, axe )
wolf_1 = Wolf("Wolf.","A large white wolf with mangled hair and bloody teath.", 30, [bite, claws])