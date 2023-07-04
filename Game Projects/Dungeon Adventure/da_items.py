class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Weapon(Item):
    def __init__(self, name, description, damage):
        super().__init__(name, description)
        self.damage = damage


class HealingPotion(Item):
    def __init__(self, name, description, healing_amount):
        super().__init__(name, description)
        self.effect = {"type": "healing", "amount": healing_amount}
        

health_potion = HealingPotion("Healing Potion", "A giga healing potion", 5)


