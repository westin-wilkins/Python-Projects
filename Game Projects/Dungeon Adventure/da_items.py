class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Weapon(Item):
    def __init__(self, name, description, damage):
        super().__init__(name, description)
        self.damage = damage

class Potion(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.effect_description = None
        self.effect = None



