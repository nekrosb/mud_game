class rooms:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.neighbours = {}
        self.items = []

    def add_neighbour(self, way, room):
        self.neighbours[way] = room

    def add_item(self, item):
        self.items.append(item)


