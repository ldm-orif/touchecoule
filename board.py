# AUTEUR : LDM
# CREATION : 30.04.2026
# contains board logic and data

from constants import ORIENTATION, CASE_STATE



class BOARD:
    def __init__(self, dimension):
        self.dimension = dimension
        self.grid = [[CASE_STATE.CLEAN for x in range(dimension)] for y in range(dimension)] # [h][w]
    
    def miss(self, case):
        self.grid[int(case.x)][int(case.y)] = CASE_STATE.MISS

    def hit(self, case):
        self.grid[int(case.x)][int(case.y)] = CASE_STATE.HIT

    def sink(self, case, length, orientation):
        if orientation == ORIENTATION.HORIZONTAL:
            for i in range(length):
                self.grid[int(case.x+i)][int(case.y)] = CASE_STATE.SUNK
        if orientation == ORIENTATION.VERTICAL:
            for i in range(length):
                self.grid[int(case.x)][int(case.y+i)] = CASE_STATE.SUNK