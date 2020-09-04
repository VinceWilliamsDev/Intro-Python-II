# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room 

class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.room = starting_room
        self.inventory = []

    def __str__(self):
        return f"{self.name} is in the {self.room.describe()}"

    def about(self):
        return self.__str__()