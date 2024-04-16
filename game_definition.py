from room import Room
from item import Item

class GameDefinition:
    def __init__(self):
        self.rooms = {}
        self.start_room = None

    def create_room(self, name, description):
        room = Room(name, description)
        self.rooms[name] = room
        if not self.start_room:
            self.start_room = room

    def create_item(self, room_name, item_name, item_description):
        item = Item(item_name, item_description)
        self.rooms[room_name].items.append(item)

    def connect_rooms(self, room1, room2, direction):
        self.rooms[room1].connections[direction] = self.rooms[room2]
        self.rooms[room2].connections[opposite_direction(direction)] = self.rooms[room1]

    def clear_game(self):
        self.rooms.clear()
        self.start_room = None

def opposite_direction(direction):
    opposites = {"north": "south", "south": "north", "east": "west", "west": "east"}
    return opposites[direction]