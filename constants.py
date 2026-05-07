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

# UI specific constants

SCREEN_WIDTH = 1024 # game windows' width
SCREEN_HEIGHT = 768 # game windows' height
CASE_DIMENSION = 40 # width and height of each case in grids
OUTLINE_THICKNESS = 5 # ships' and selected case outline

#TODO HERE: ADD USUAL TEXT FONT AND SIZE (AND THE IA LOG VARIANT IF IT IS NEEDED)

class UI_TEXT:
    # Game screen text
    PLAYER_ROUND_1 = "Tour "
    PLAYER_ROUND_2A = " du joueur 1"
    PLAYER_ROUND_2B = " du joueur 2"
    PLAYER_TERRAIN = "Votre terrain"
    OPPONENT_TERRAIN = "Terrain ennemie"
    OPPONENT_SHIPS_LEFT = "Navires ennemie restant : "
    SHOT_INFO_CAN_SHOOT = "Vous pouvez tirer"
    SHOT_INFO_CANNOT_SHOOT = "Vous ne pouvez plus tirer"
    SHOT_INFO_WON = "Aucun bateau ennemie restant"
    END_TURN_AVAILABLE = "Terminer le tour"
    END_TURN_UNAVAILABLE = "Veuillez tirer"


class UI_COLORS:
    BACKGROUND_COLOR = GRAY

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

# multi-domain constants

GRID_SIZE = 10
SHIP_PER_PLAYER = 5
IA_LOG_LINE_LIMIT = 20
IA_LOG_CHARACTER_PER_LINE_LIMIT = 50

class ORIENTATION(Enum):
    HORIZONTAL = False
    VERTICAL = True

class CASE_STATE(Enum):
    CLEAN = 0
    MISS = 1
    HIT = 1
    SUNK = 2

#TODO HERE: SHIP NAMES AND SIZES