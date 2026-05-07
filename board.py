# AUTEUR : LDM
# CREATION : 30.04.2026
# contains board logic and data

from enum import Enum
from constants import ORIENTATION, CASE_STATE



class BOARD:
    def __init__(self, dimension):
        self.dimension = dimension
        self.grid = [[CASE_STATE.CLEAN for x in range(dimension)] for y in range(dimension)] # [h][w]
    
    def miss(self, case):
        self.grid[case[0]][case[1]] = CASE_STATE.MISS

    def hit(self, case):
        self.grid[case[0]][case[1]] = CASE_STATE.HIT

    def sink(self, case, length, orientation):
        if orientation == ORIENTATION.HORIZONTAL:
            for i in range(length):
                self.grid[case[0]][case[1]+i] = CASE_STATE.SUNK
        if orientation == ORIENTATION.VERTICAL:
            for i in range(length):
                self.grid[case[0]+i][case[1]] = CASE_STATE.SUNK