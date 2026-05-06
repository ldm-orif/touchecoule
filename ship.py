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
            case 1:
                self.length = 5
                self.name = "Porte-avions"
            case 2:
                self.length = 4
                self.name = "Croiseur"
            case 3:
                self.length = 3
                self.name = "Contre-Torpilleur"
            case 4:
                self.length = 3
                self.name = "Sous-marin"
            case _:
                self.length = 2
                self.name = "Torpilleur"
        self.cases_hit = [False for x in self.length]

    def hit(self,case):
        self.cases_hit[case] = True
        if False not in self.cases_hit:
            self.sunk = True