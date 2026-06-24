# AUTEUR : LDM
# CREATION : 30.04.2026
# Contains ship details

from pygame import Vector2
from constants import ORIENTATION


class SHIP:
    def __init__(self,type):
        self.position = Vector2(-1,-1) # always indicate the most top-right case of the ship
        self.orientation = ORIENTATION.HORIZONTAL
        self.sunk = False
        match type:
            case 0:
                self.length = 5
                self.name = "Porte-avions"
            case 1:
                self.length = 4
                self.name = "Croiseur"
            case 2:
                self.length = 3
                self.name = "Contre-Torpilleur"
            case 3:
                self.length = 3
                self.name = "Sous-marin"
            case _:
                self.length = 2
                self.name = "Torpilleur"
        self.cases_hit = [False for x in range(self.length)]

    def hit(self,case):
        self.cases_hit[case] = True
        if False not in self.cases_hit:
            self.sunk = True

    # return cases the ship occupies
    def get_occupied_cases(self):
        occupied_cases = []
        for i in range(self.length):
            if self.orientation == ORIENTATION.HORIZONTAL:
                occupied_cases.append(Vector2(self.position.x+i,self.position.y))
            else:
                occupied_cases.append(Vector2(self.position.x,self.position.y+i))
        return occupied_cases
