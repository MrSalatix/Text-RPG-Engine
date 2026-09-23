import random

from enemy_generator import generate_enemy
from room import Room

room_types = ['Enemy', 'Empty']


class Dungeon:
    def __init__(self):
        self.rooms = []
        self.current_room_index = 0

    def add_room(self, room):
        self.rooms.append(room)

    def describe_dungeon(self):
        print("=============Dungeon==============")
        for index, room in enumerate(self.rooms, start=1):
            print(f'Комната {index}: {room.room_type}')
        print("==================================")

    def generate_dungeon(self, amount):
        self.rooms = []
        self.current_room_index = 0
        if amount > 0:
            for i in range(amount):
                raw_choice = random.choice(room_types)
                if raw_choice == 'Empty':
                    self.add_room(Room('Empty'))
                elif raw_choice == 'Enemy':
                    self.add_room(Room('Enemy', generate_enemy()))



