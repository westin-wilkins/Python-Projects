class Weapon:
    def __init__(self, name, type, damage, affinity=0, element=None, element_damage=None):
        self.name = name
        self.type = type
        self.damage = damage
        self.element = element
        self.element_damage = element_damage
        self.affinity = affinity