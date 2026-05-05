# AUTEUR : LDM
# CREATION : 30.04.2026
# contain the logic related to the gameplay

from enum import Enum


class Gamemode(Enum): # Used to know the current gamemode
    PVP = 1 # Player versus Player
    PVC = 2 # Player versus Computer

class Stage(Enum): # Used to determine which screen to show
    TITLE = 0 # Title screen
    PLACEMENT = 1 # Placement screen
    GAME = 2 # Game screen, what you see when you think about "touché coulé"
    TRANSITION = 3 # Transition screen, skipped if in PVC
    VICTORY = 4 # End of game screen
    
class GAME:
    def __init__(self):
        self.quitting = False # Used by main.py to know if the user clicked on the "Quit game" button
        self.gamemode = Gamemode.PVP # Used to determine the 2nd opponent's type , defaults to PVP
        self.stage = Stage.TITLE # Current stage/screen of the game
        self.turn = 0 # Current turn of the game, 0 is the placement "turn"
        self.has_torpedo = False # Indicate if, during the GAME stage, can the current player shoot
        self.is_player_1_turn = True # Indicate if Player 1 is currently playing (True) or Player 2 (False)

        self.player_1 = "TODO" # Player that always start first, always human player #TODO DECLARE CORRECT VALUE
        self.player_2 = "TODO" # Second player, whose used by the IA in PVC          #TODO DECLARE CORRECT VALUE
        self.ui = "TODO" # UI of the game, also referred to as "IHM"                 #TODO DECLARE CORRECT VALUE
        self.ai = "TODO" # Behavior of the Computer player during PVC                #TODO DECLARE CORRECT VALUE
        
    def reset(self): # Called to return to title screen after the victory screen
        a=1 #TODO PUT ALL VALUES BACK TO DEFAULT

    def ai_act(self): # Called to indicate the AI can make the next step (equivalant of a line in it's log)
        a=1 #TODO CALL AI AND TELL IT TO ACT

    def on_click(self, pos):
        a=1 #TODO ASK UI WHAT IS HIT, THEN CALL RELEVANT METHOD

    def draw_everything(self): # Called to ask UI to draw the visuals
        a=1 #TODO ASK UI TO DRAW A CERTAIN SCREEN, PASSSING ONLY RELEVANT INFORMATION THAT CAN INCLUDE GAMEMODE, TURN, HAS_TORPEDO, ETC.

    
    

# MISSING : GAMEMODE CHANGE | PLAY ORDER TRACKING | STAGE CHANGE | TURN CHANGE
