class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {"north": None, "east": None, "south": None, "west": None}
        self.contents = []
        self.enemies_in_room = []