# AUTEUR : LDM
# CREATION : 30.04.2026
# Contains the player's data

from constants import GRID_SIZE, SHIP_PER_PLAYER, ORIENTATION, CASE_STATE
from board import BOARD
from ship import SHIP
from pygame import Vector2

class PLAYER:
    def __init__(self):
        self.board = BOARD(GRID_SIZE)
        self.ships = [SHIP(x) for x in range(SHIP_PER_PLAYER)]
        self.selected_case = Vector2(-1,-1)
        self.selected_ship = -1

    def nb_ship_unsunk(self):
        nb_unsunk = 0
        for i in range(SHIP_PER_PLAYER):
            if not self.ships[i].sunk:
                nb_unsunk += 1
        return nb_unsunk
    
    def launch(self, aimed_case): # return True if a ship is hit, return False if not
        for ship in self.ships:
            if ship.orientation == ORIENTATION.HORIZONTAL:
                if aimed_case.y == ship.position.y:
                    for i in range(ship.length):
                        if aimed_case.x == ship.position.x +i:
                            ship.hit(aimed_case)
                            if ship.sunk:
                                self.board.sink(ship.position, ship.length, ship.orientation)
                            self.selected_case = Vector2(-1,-1)
                            return True
            if ship.orientation == ORIENTATION.VERTICAL:
                if aimed_case.x == ship.position.x:
                    for i in range(ship.length):
                        if aimed_case.y == ship.position.y +i:
                            ship.hit(aimed_case)
                            if ship.sunk:
                                self.board.sink(ship.position, ship.length, ship.orientation)
                            self.selected_case = Vector2(-1,-1)
                            return True
        self.board.miss(aimed_case)
        return False
    
    def aim(self, case): # change selected case, return True if case is a valid target (inside grid, position never launched at), False otherwise
        a=1

    def place(self, ship_type, orientation):
        a=1

    def remove(self, ship_type):
        a=1

    def collides(self): # check if selected_ship ship collides with other ships
        a=1