# AUTEUR : LDM
# CREATION : 30.04.2026
# contain the logic related to the gameplay

from enum import Enum
from player import PLAYER
from ui import UI
from ai import AI


class Gamemode(Enum): # Used to know the current gamemode
    PVP = 1 # Player versus Player
    PVC = 2 # Player versus Computer

class Stage(Enum): # Used to determine which screen to show
    TITLE = 0 # Title screen
    PLACEMENT = 1 # Placement screen
    GAME = 2 # Game screen, what you see when you think about "touché coulé"
    TRANSITION = 3 # Transition screen, skipped if in PVC
    VICTORY = 4 # End of game screen

class Placement_mode(Enum): # Used to know, during the placement stage of the game, if we wanst to place/select or delete a ship
    SELECTION = 0 # placement/ship-seletion mode
    DELETION = 1 # ship deletion mode
    
class GAME:
    def __init__(self, surface):
        self.quitting = False # Used by main.py to know if the user clicked on the "Quit game" button
        self.gamemode = Gamemode.PVP # Used to determine the 2nd opponent's type , defaults to PVP
        self.stage = Stage.TITLE # Current stage/screen of the game
        self.turn = 0 # Current turn of the game, 0 is the placement "turn"
        self.has_torpedo = False # Indicate if, during the GAME stage, can the current player shoot
        self.placement_mode = Placement_mode.SELECTION # function of a click during the placement stage
        self.is_player_1_turn = True # Indicate if Player 1 is currently playing (True) or Player 2 (False)

        self.player_1 = PLAYER() # Player that always start first, always human player
        self.player_2 = PLAYER() # Second player, whose used by the IA in PVC
        self.ui = UI(surface) # UI of the game, also referred to as "IHM"
        self.ai = AI(self.player_2) # Behavior of the Computer player during PVC
        
    def reset(self): # Called to return to title screen after the victory screen
        self.quitting = False # Used by main.py to know if the user clicked on the "Quit game" button
        self.gamemode = Gamemode.PVP # Used to determine the 2nd opponent's type , defaults to PVP
        self.stage = Stage.TITLE # Current stage/screen of the game
        self.turn = 0 # Current turn of the game, 0 is the placement "turn"
        self.has_torpedo = False # Indicate if, during the GAME stage, can the current player shoot
        self.is_player_1_turn = True # Indicate if Player 1 is currently playing (True) or Player 2 (False)

        self.player_1 = PLAYER() # Player that always start first, always human player
        self.player_2 = PLAYER() # Second player, whose used by the IA in PVC

    def ai_act(self): # Called to indicate the AI can make the next step (equivalant of a line in it's log)
        a=1 #TODO CALL AI AND TELL IT TO ACT

    def on_click(self, pos):
        a=1 #TODO ASK UI WHAT IS HIT, THEN CALL RELEVANT METHOD

    def draw_everything(self): # Called to ask UI to draw the visuals
        a=1 #TODO ASK UI TO DRAW A CERTAIN SCREEN, PASSSING ONLY RELEVANT INFORMATION THAT CAN INCLUDE GAMEMODE, TURN, HAS_TORPEDO, ETC.

    
    

# MISSING : GAMEMODE CHANGE | PLAY ORDER TRACKING | STAGE CHANGE | TURN CHANGE
