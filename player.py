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
        self.selected_case = Vector2(-1,-1) # indicates where the player aimed on ANY grid, not specifically his own
        self.selected_ship = 0

    def nb_ship_unsunk(self):
        nb_unsunk = 0
        for i in range(SHIP_PER_PLAYER):
            if not self.ships[i].sunk:
                nb_unsunk += 1
        return nb_unsunk
    
    def launch(self): # return True if a ship is hit, return False if not
        for ship in self.ships:
            if ship.orientation == ORIENTATION.HORIZONTAL:
                if self.selected_case.y == ship.position.y:
                    for i in range(ship.length):
                        if self.selected_case.x == ship.position.x +i:
                            ship.hit(self.selected_case)
                            if ship.sunk:
                                self.board.sink(ship.position, ship.length, ship.orientation)
                            self.selected_case = Vector2(-1,-1)
                            return True
            if ship.orientation == ORIENTATION.VERTICAL:
                if self.selected_case.x == ship.position.x:
                    for i in range(ship.length):
                        if self.selected_case.y == ship.position.y +i:
                            ship.hit(self.selected_case)
                            if ship.sunk:
                                self.board.sink(ship.position, ship.length, ship.orientation)
                            self.selected_case = Vector2(-1,-1)
                            return True
        self.board.miss(self.selected_case)
        return False
    
    def aim(self, case): # change selected case, return True if case is a valid target (inside grid, position never launched at), False otherwise
        self.selected_case = case

    def select(self, variant):
        self.selected_ship = variant

    def place(self, case): # try to place selected ship at indicated case without causing a collision
        old_position = self.ships[self.selected_ship].position
        self.ships[self.selected_ship].position = case
        if self.collides():
            self.ships[self.selected_ship].position = old_position
            return False
        return True

    def rotate(self, to_the_right): # try to rotate selected ship without causing a collision, can freely rotate unplaced ships
        if to_the_right and self.ships[self.selected_ship].orientation == ORIENTATION.HORIZONTAL:
            self.ships[self.selected_ship].orientation = ORIENTATION.VERTICAL
            if self.collides() and not (self.ships[self.selected_ship].position.x < 0 and self.ships[self.selected_ship].position.y < 0):
                self.ships[self.selected_ship].orientation = ORIENTATION.HORIZONTAL
                return False
            return True
        elif not to_the_right and self.ships[self.selected_ship].orientation == ORIENTATION.VERTICAL:
            self.ships[self.selected_ship].orientation = ORIENTATION.HORIZONTAL
            if self.collides() and not (self.ships[self.selected_ship].position.x < 0 and self.ships[self.selected_ship].position.y < 0):
                self.ships[self.selected_ship].orientation = ORIENTATION.VERTICAL
                return False
            return True


    def remove(self, variant):
        a=1 #TODO

    def collides(self): # check if selected_ship ship collides with other ships
        ship_cases = self.ships[self.selected_ship].get_occupied_cases()

        #check each concerned case
        collides = False

        for my_case in ship_cases:
            if collides: break
            collides = my_case.x >= GRID_SIZE or my_case.y >= GRID_SIZE or my_case.x < 0 or my_case.y < 0
        for ship in self.ships:
            if ship.name == self.ships[self.selected_ship].name: continue
            if collides: break
            for case in ship.get_occupied_cases():
                if collides: break
                for our_case in ship_cases:
                    if collides: break
                    collides = case.x == our_case.x and case.y == our_case.y
        return collides