import descr_rooms

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


room1 = rooms(descr_rooms.room_name1, descr_rooms.room_description1)

room2 = rooms(descr_rooms.room_name2, descr_rooms.room_description2)

room3 = rooms(descr_rooms.room_name3, descr_rooms.room_description3)

room4 = rooms(descr_rooms.room_name4, descr_rooms.room_description4)

room5 = rooms(descr_rooms.room_name5, descr_rooms.room_description5)

room6 = rooms(descr_rooms.room_name6, descr_rooms.room_description6)

room7 = rooms(descr_rooms.room_name7, descr_rooms.room_description7)

room8 = rooms(descr_rooms.room_name8, descr_rooms.room_description8)

room9 = rooms(descr_rooms.room_name9, descr_rooms.room_description9)

room10 = rooms(descr_rooms.room_name10, descr_rooms.room_description10)