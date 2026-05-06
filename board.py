# AUTEUR : LDM
# CREATION : 30.04.2026
# contains board logic and data

from enum import Enum
from constants import ORIENTATION

class Case_State(Enum):
    CLEAN = 0
    MISS = 1
    HIT = 1
    SUNK = 2

class BOARD:
    def __init__(self, dimension):
        self.dimension = dimension
        self.grid = [[Case_State.CLEAN for x in range(dimension)] for y in range(dimension)] # [h][w]
    
    def miss(self, case):
        self.grid[case[0]][case[1]] = Case_State.MISS

    def hit(self, case):
        self.grid[case[0]][case[1]] = Case_State.HIT

    def sink(self, case, length, orientation):
        if orientation == ORIENTATION.HORIZONTAL:
            for i in range(length):
                self.grid[case[0]][case[1]+i] = Case_State.SUNK
        if orientation == ORIENTATION.VERTICAL:
            for i in range(length):
                self.grid[case[0]+i][case[1]] = Case_State.SUNK