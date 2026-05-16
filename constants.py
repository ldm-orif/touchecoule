# AUTEUR : LDM
# CREATION : 30.04.2026
# Contain the constants used about everywhere else in the code

from enum import Enum

# Colors

BLUE = (0,148,255)
DARK_BLUE = (0,38,255)
LIGHT_GRAY = (226,222,222)
GRAY = (128,128,128)
DARK_GRAY = (64,64,64)
YELLOW = (255,216,0)
RED = (255,0,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (182,255,0)

# UI specific constants

SCREEN_WIDTH = 1024 # game windows' width
SCREEN_HEIGHT = 768 # game windows' height
CASE_DIMENSION = 40 # width and height of each case in grids
ICON_DIMENSION = 2*CASE_DIMENSION # width and height of icons
OUTLINE_THICKNESS = 5 # ships' and selected case outline

#TODO HERE: ADD USUAL TEXT FONT AND SIZE (AND THE IA LOG VARIANT IF IT IS NEEDED)

class UI_TEXT:
    FONT = 'Font/PoetsenOne-Regular.ttf'

    # Title screen text
    TITLE_PART_1 = "BATAILLE"
    TITLE_PART_2 = "NAVALLE"
    TITLE_PVP_1 = "JOUEUR"
    TITLE_PVP_2 = "CONTRE"
    TITLE_PVP_3 = "JOUEUR"
    TITLE_PVC_1 = "JOUEUR"
    TITLE_PVC_2 = "CONTRE"
    TITLE_PVC_3 = "MACHINE"
    TITLE_QUIT = "QUITTER"

    # Placement screen text
    PLACEMENT_INFO = "Posez tous les bateaux pour continuer"
    PLACEMENT_PLAYER_A = "Joueur 1"
    PLACEMENT_PLAYER_B = "Joueur 2"

    # Game screen text
    GAME_PLAYER_ROUND_1 = "Tour "
    GAME_PLAYER_ROUND_2A = " du joueur 1"
    GAME_PLAYER_ROUND_2B = " du joueur 2"
    GAME_PLAYER_TERRAIN = "Votre terrain"
    GAME_OPPONENT_TERRAIN = "Terrain ennemie"
    GAME_OPPONENT_SHIPS_LEFT = "Navires ennemie restant : "
    GAME_SHOT_INFO_CAN_SHOOT = "Vous pouvez tirer"
    GAME_SHOT_INFO_CANNOT_SHOOT = "Vous ne pouvez plus tirer"
    GAME_SHOT_INFO_WON = "Aucun bateau ennemie restant"
    GAME_END_TURN_AVAILABLE = "Terminer le tour"
    GAME_END_TURN_UNAVAILABLE = "Veuillez tirer"

    # Transition screen text
    TRANSITION_PASS_KEYBOARD_TO = "PASSEZ LE CLAVIER AU "
    TRANSITION_CONTINUE = "JE SUIS "
    TRANSITION_PLAYER_A = "JOUEUR 1"
    TRANSITION_PLAYER_B = "JOUEUR 2"

    # AI screen text
    AI_ROUND_1 = "Tour "
    AI_ROUND_2 = " de l'IA"
    AI_PLAYER_TERRAIN = "Votre terrain"
    AI_LOGS_HEADER = "Actions de l'IA"
    AI_CONTINUE = "Continuer"
    AI_WAIT = "Attendez"

    # End screen text
    VICTORY_WINNER_1 = "Victoire "
    VICTORY_WINNER_2 = " !"
    VICTORY_TERRAIN_OF = "Terrain "
    VICTORY_PLAYER_A = "du joueur 1"
    VICTORY_PLAYER_B = "du joueur 2"
    VICTORY_AI = "de l'IA"
    VICTORY_CONTINUE = "Continuer"

class UI_ICONS:
    FOLDER = 'SVG/'

    # case states
    CASE_HIT = "case-hit.svg"
    CASE_MISS = "case-miss.svg"
    CASE_SELECTED = "case-selected.svg"
    CASE_SUNK = "case-sunk.svg"
    
    # buttons
    LAUNCH_ON = "launch.svg"
    LAUNCH_OFF = "no-launch.svg"
    SELECTION_ON = "selection-active.svg"
    SELECTION_OFF = "selection.svg"
    DELETE_ON = "delete-active.svg"
    DELETE_OFF = "delete.svg"
    ROTATE_LEFT = "rotate-left.svg"
    ROTATE_RIGHT = "rotate-right.svg"
    CONFIRM_ON = "confirmation-active.svg"
    CONFIRM_OFF = "confirmation.svg"


class UI_COLORS:
    BACKGROUND_COLOR = GRAY
    TITLE_COLOR = GREEN
    TITLE_BUTTON_COLOR = GRAY

    OCEAN_COLOR_PRIMARY = BLUE
    OCEAN_COLOR_SECONDARY = DARK_BLUE

    TEXT_COLOR = LIGHT_GRAY
    ICON_COLOR = LIGHT_GRAY
    GRAPHIC_BACKGROUND_COLOR = DARK_GRAY

    BOAT_OUTLINE_COLOR = LIGHT_GRAY
    BOAT_INSIDE_COLOR = GRAY

    SINKED_BOAT_OUTLINE_COLOR = GRAY
    SINKED_BOAT_INSIDE_COLOR = DARK_GRAY

    SELECTED_COLOR = YELLOW
    MISS_COLOR = WHITE
    HIT_COLOR = RED
    SINKED_COLOR = BLACK

    AI_LOGS_TEXT_COLOR = BLACK
    AI_LOGS_BACKGROUND_COLOR = LIGHT_GRAY

# multi-domain constants

GRID_SIZE = 10
SHIP_PER_PLAYER = 5
IA_LOG_LINE_LIMIT = 10
IA_LOG_CHARACTER_PER_LINE_LIMIT = 50

class ORIENTATION(Enum):
    HORIZONTAL = False
    VERTICAL = True

class CASE_STATE(Enum):
    CLEAN = 0
    MISS = 1
    HIT = 2
    SUNK = 3

class GAMEMODE(Enum): # Used to know the current gamemode
    PVP = 1 # Player versus Player
    PVC = 2 # Player versus Computer

class PLACEMENT_MODE(Enum): # Used to know, during the placement stage of the game, if we wanst to place/select or delete a ship
    SELECTION = 0 # placement/ship-seletion mode
    DELETION = 1 # ship deletion mode

class BUTTONS(Enum):
    # title
    TITLE_PVP = 0
    TITLE_PVC = 1
    TITLE_QUIT = 2

    # placement
    PLACEMENT_SELECTION = 3
    PLACEMENT_DELETION = 4
    PLACEMENT_ROTATE_LEFT = 5
    PLACEMENT_ROTATE_RIGHT = 6
    PLACEMENT_CONTINUE = 7

    # game
    GAME_LAUNCH = 8
    GAME_CONTINUE = 9

    # transition
    TRANSITION_CONTINUE = 10

    # ai
    AI_CONTINUE = 11

    # victory
    VICTORY_CONTINUE = 12

class AI_LOGS_TEXT(Enum):
    START = "LOGS DES TIRS DE L'IA"
    AIM = "L'IA TIRE SUR LA CASE"
    HIT = "TOUCHÉ !"
    MISS = "LOUPÉ !"
    SINK_1 = "COULÉ ! IL VOUS RESTE "
    SINK_2 = " BATEAUX"
    END_1 = "L'IA A TERMIN´3 SON TOUR,"
    END_2 = "APPUYEZ SUR 'CONTINUER'"