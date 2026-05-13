# AUTEUR : LDM
# CREATION : 30.04.2026
# Contains every visuals and screens

# TODO USE THE SCREEN OF THE IA TURN ALSO FOR PLACEMENT TURN !

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, CASE_DIMENSION, ICON_DIMENSION, GRID_SIZE, PLACEMENT_MODE, GAMEMODE, CASE_STATE, BUTTONS, ORIENTATION, UI_COLORS as COLORS, UI_TEXT as TEXTS, UI_ICONS as ICONS
import pygame
from pygame import Vector2

class UI:
    def __init__(self, surface):
        self.current_buttons = [] # single list containing the tuple (rect,button's id)
        self.current_interactible_grid_cases = [[]] # is double list than contains the rect
        self.current_interactible_ships = [] # single list containing the tuple (rect,variant)
        self.screen = surface

    def draw_title(self):
        self.current_buttons = []
        self.current_interactible_grid_cases = [[]]
        self.current_interactible_ships = []
        self.screen.fill(COLORS.BACKGROUND_COLOR)

    def draw_placement(self, is_player_1, player): #note: in PVC, for the computer's turn, we show draw_ai_turn
        self.current_buttons = []
        self.current_interactible_grid_cases = [[]]
        self.current_interactible_ships = []
        self.screen.fill(COLORS.BACKGROUND_COLOR) # FOR PLACEMENT COLLISION : COLLISION CHECK WITH SHIP FIRST

    def draw_game(self, is_player_1, turn, has_shot_left, player, opponent):
        self.current_buttons = []
        self.current_interactible_grid_cases = [[]]
        self.current_interactible_ships = []
        self.screen.fill((COLORS.BACKGROUND_COLOR))

        # grids
        player_grid_position = Vector2(2,4)
        opponent_grid_position = Vector2(4+GRID_SIZE, 4)

        self.draw_grid(player_grid_position, False) # player's grid
        self.draw_grid(opponent_grid_position, True) # opponent's grid


        # ships
        self.draw_ships_on_grid(player_grid_position, player.ships, -1) # player's ship


        # cases' state
        self.draw_grid_states(player_grid_position, player.board.grid, Vector2(-1,-1)) # player's grid state
        self.draw_grid_states(opponent_grid_position, opponent.board.grid, player.selected_case) # opponent's grid state + aimed case


        # text and buttons

        turn_text = TEXTS.PLAYER_ROUND_1 + str(turn)
        turn_text_position = Vector2(player_grid_position.x-1,1)
        turn_text_width = opponent_grid_position.x + GRID_SIZE
        turn_text_height = 1
        if is_player_1 : turn_text += TEXTS.PLAYER_ROUND_2A
        else : turn_text += TEXTS.PLAYER_ROUND_2B
        self.draw_text(turn_text, turn_text_position, turn_text_width, turn_text_height, False) # "tour x du joueur y"


        grid_text_width = GRID_SIZE
        grid_text_height = 1  

        player_grid_text = TEXTS.PLAYER_TERRAIN
        opponent_grid_text = TEXTS.OPPONENT_TERRAIN
        player_grid_text_position = Vector2(player_grid_position.x, player_grid_position.y -1)
        opponent_grid_text_position = Vector2(opponent_grid_position.x, opponent_grid_position.y -1)
        self.draw_text(player_grid_text, player_grid_text_position, grid_text_width, grid_text_height, False) # "votre terrain"
        self.draw_text(opponent_grid_text, opponent_grid_text_position, grid_text_width, grid_text_height, False) # "terrain enemie"


        info_text_width = GRID_SIZE
        info_text_height = 1

        info_ship_text = TEXTS.OPPONENT_SHIPS_LEFT + str(opponent.nb_ship_unsunk())
        info_ship_text_position = Vector2(player_grid_position.x, player_grid_position.y + GRID_SIZE + 0.5)
        self.draw_text(info_ship_text, info_ship_text_position, info_text_width, info_text_height, False) # "navires enemie restant : z"

        info_shot_text = ""
        if opponent.nb_ship_unsunk() <= 0: info_shot_text = TEXTS.SHOT_INFO_WON
        elif has_shot_left: info_shot_text = TEXTS.SHOT_INFO_CAN_SHOOT
        else: info_shot_text = TEXTS.SHOT_INFO_CANNOT_SHOOT
        info_shot_text_position = Vector2(info_ship_text_position.x, info_ship_text_position.y + info_text_height +0.5) # texts with shot info
        self.draw_text(info_shot_text, info_shot_text_position, info_text_width, info_text_height, False)
        

        btn_height = 2

        end_turn_text = ""
        if has_shot_left : end_turn_text = TEXTS.END_TURN_UNAVAILABLE
        else: end_turn_text = TEXTS.END_TURN_AVAILABLE
        end_turn_text_width = 5
        end_turn_text_position = Vector2(opponent_grid_position.x + GRID_SIZE - end_turn_text_width, opponent_grid_position.y + GRID_SIZE +1)
        self.draw_text(end_turn_text, end_turn_text_position, end_turn_text_width, btn_height, True) # "Terminer le tour"

        # button with icon

        # "shoot" button
        #TODO

    def draw_transition(self, next_player):
        self.current_buttons = []
        self.current_interactible_grid_cases = [[]]
        self.current_interactible_ships = []
        self.screen.fill(COLORS.BACKGROUND_COLOR)

    def draw_ia(self, turn_text, human_player, ia): #note: turn here will be transformed to str, so that "placement" can be passed
        self.current_buttons = []
        self.current_interactible_grid_cases = [[]]
        self.current_interactible_ships = []
        self.screen.fill(COLORS.BACKGROUND_COLOR)

    def draw_victory(self, player_1, player_2, gamemode):
        self.current_buttons = []
        self.current_interactible_grid_cases = [[]]
        self.current_interactible_ships = []
        self.screen.fill(COLORS.BACKGROUND_COLOR)

    def draw_grid(self, position, interactible):
        new_interactible_cases = []
        
        for row in range(GRID_SIZE):
            new_interactible_cases.append([])
            if row % 2 == 0:
                for col in range(GRID_SIZE):
                    rect = pygame.Rect((col+position.x)*CASE_DIMENSION, (row+position.y)*CASE_DIMENSION, CASE_DIMENSION, CASE_DIMENSION)
                    chosen_color = COLORS.OCEAN_COLOR_SECONDARY
                    if col % 2 == 0:
                        chosen_color = COLORS.OCEAN_COLOR_PRIMARY
                    new_interactible_cases[row].append(rect)
                    pygame.draw.rect(self.screen,chosen_color,rect)

            else:
                for col in range(GRID_SIZE):
                    rect = pygame.Rect((col+position.x)*CASE_DIMENSION, (row+position.y)*CASE_DIMENSION, CASE_DIMENSION, CASE_DIMENSION)
                    chosen_color = COLORS.OCEAN_COLOR_PRIMARY
                    if col % 2 == 0:
                        chosen_color = COLORS.OCEAN_COLOR_SECONDARY
                    new_interactible_cases[row].append(rect)
                    pygame.draw.rect(self.screen,chosen_color,rect)

        if interactible:
            self.current_interactible_grid_cases = new_interactible_cases

    def draw_ships_on_grid(self, grid_position, ships, selected_ship): # ships on the grid are never interactible
        for variant in range(len(ships)):
            ship = ships[variant]
            if (ship.position.x >= 0 and ship.position.x < GRID_SIZE) and (ship.position.y >= 0 and ship.position.y < GRID_SIZE):
                position = Vector2(grid_position.x + ship.position.x, grid_position.y + ship.position.y)
                self.draw_ship(position, ship.length, ship.orientation, ship.sunk, False, variant == selected_ship, variant)

    def draw_ship(self, position, length, orientation, sunk, interactible, selected, variant): # draw a singular ship and returns it
        # note : selected ship are not interactible
        inline_padding = 5
        length_x = 1
        length_y = 1
        if orientation == ORIENTATION.HORIZONTAL: length_x = length
        else: length_y = length
        
        ship_outline_rect = pygame.Rect(position.x*CASE_DIMENSION, position.y*CASE_DIMENSION, length_x*CASE_DIMENSION, length_y*CASE_DIMENSION)
        ship_inside_rect = pygame.Rect(position.x*CASE_DIMENSION+inline_padding, position.y*CASE_DIMENSION+inline_padding, length_x*CASE_DIMENSION-2*inline_padding, length_y*CASE_DIMENSION-2*inline_padding)

        outline_color = COLORS.BOAT_OUTLINE_COLOR
        inside_color = COLORS.BOAT_INSIDE_COLOR
        if sunk:
            outline_color = COLORS.SINKED_BOAT_OUTLINE_COLOR
            inside_color = COLORS.SINKED_BOAT_INSIDE_COLOR
        if selected:
            outline_color = COLORS.SELECTED_COLOR

        if interactible and not selected:
            self.current_interactible_ships.append((ship_outline_rect,variant))

        pygame.draw.rect(self.screen,outline_color,ship_outline_rect)
        pygame.draw.rect(self.screen,inside_color,ship_inside_rect)

    def draw_grid_states(self, position, cases_state, selected_position): # if selected_position -1;-1 then simply don't draw it
        a=1

    def draw_icon(self, icon, position, dimension_x, dimension_y, selected):
        a=1

    def draw_text(self, text, position, dimension_x, dimension_y, interatible): # text and buttons
        background_rect = pygame.Rect(position.x*CASE_DIMENSION, position.y*CASE_DIMENSION, dimension_x*CASE_DIMENSION, dimension_y*CASE_DIMENSION)
        if interatible:
            a=1 #TODO: ADD BACKGROUND_RECT AS THE INTERACTIBLE 
        pygame.draw.rect(self.screen,COLORS.GRAPHIC_BACKGROUND_COLOR,background_rect)

        game_font = pygame.font.Font(TEXTS.FONT, 25)
        text_surface = game_font.render(text, True, COLORS.TEXT_COLOR)
        text_rect = text_surface.get_rect(center= ((position.x+(0.5*dimension_x))*CASE_DIMENSION, (position.y+(0.5*dimension_y))*CASE_DIMENSION))
        self.screen.blit(text_surface,text_rect)
    
    def draw_logs(self, logs, position, dimension_x, dimension_y): # specific to AI logs
        a=1

    