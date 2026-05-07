# AUTEUR : LDM
# CREATION : 30.04.2026
# Contains the computer opponent's data and logic

from constants import SHIP_PER_PLAYER, ORIENTATION, GRID_SIZE, IA_LOG_LINE_LIMIT, IA_LOG_CHARACTER_PER_LINE_LIMIT
from player import PLAYER
from random import randint
from pygame import Vector2

class AI:
    def __init__(self, player):
        self.player = PLAYER()
        self.logs = 1 #TODO ADD STRING LIMIT HERE

    def add_log(self, text):
        a=1

    def clean_log(self):
        a=1

    def placement_behavior(self): #TODO: ADD LOG LINE FOR EACH BOAT PLACED
        placed = 0

        while placed < SHIP_PER_PLAYER:
            self.player.selected_ship = placed

            orientation = randint(0,1)
            if orientation < 1:
                orientation = ORIENTATION.HORIZONTAL
            else :
                orientation = ORIENTATION.VERTICAL

            position = Vector2(float(randint(0,GRID_SIZE-1)),float(randint(0,GRID_SIZE-1)))

            self.player.ships[self.player.selected_ship].orientation = orientation
            self.player.ships[self.player.selected_ship].position = position

            if not self.player.collides():
                placed+=1

        self.player.selected_ship = -1


    def turn_behavior(self):
        a=1