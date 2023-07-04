class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Effect:
    def __init__(self, type):
        self.type = type


class Weapon(Item):
    def __init__(self, name, description, damage):
        super().__init__(name, description)
        self.damage = damage


class Potion(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.effect_description = None
        self.effect = Effect(None)
    
    def healing(self, player):
        if self.effect == "healing":
            player.health += healing_potion.healing_amount


class HealingPotion(Potion):
    def __init__(self, name, description, healing_amount):
        super().__init__(name, description)
        self.healing_amount = healing_amount



healing_potion = HealingPotion("Healing Potion", "A giga healing potion", 5)
healing_potion.effect = "healing"
        

