class Enemies:
    def __init__(self, name, description, health, equipped):
        self.name = name
        self.description = description
        self.health = health
        self.equipped = equipped
        self.encounter_dialogue = None
        self.contents = []
