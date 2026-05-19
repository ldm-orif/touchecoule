# AUTEUR : LDM
# CREATION : 30.04.2026
# Contains the computer opponent's data and logic

from enum import Enum
from constants import SHIP_PER_PLAYER, ORIENTATION, GRID_SIZE, IA_LOG_LINE_LIMIT, IA_LOG_CHARACTER_PER_LINE_LIMIT, AI_LOGS_TEXT, CASE_STATE
from random import randint
from pygame import Vector2

class Hit_direction(Enum):
    UNKNOWN = 0
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class AI:
    def __init__(self, player, game):
        self.player = player
        self.logs = []
        self.last_hit = Vector2(-1,-1) # last successful hit (put to [-1;-1] if has sunk)
        self.last_hit_direction = Hit_direction.UNKNOWN
        self.game = game
        self.turn_finished = False

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