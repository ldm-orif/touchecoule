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
        self.load_icons() # list with Tuple (UI_ICONS, source)

    def load_icons(self): # convert to alpha all icons so they don't have to be sommuned in the runtime
        self.launch_on = pygame.transform.smoothscale(pygame.image.load(ICONS.FOLDER + ICONS.LAUNCH_ON).convert_alpha(), (ICON_DIMENSION, ICON_DIMENSION))
        self.launch_off = pygame.transform.smoothscale(pygame.image.load(ICONS.FOLDER + ICONS.LAUNCH_OFF).convert_alpha(), (ICON_DIMENSION, ICON_DIMENSION))
        self.selection_on = pygame.transform.smoothscale(pygame.image.load(ICONS.FOLDER + ICONS.SELECTION_ON).convert_alpha(), (ICON_DIMENSION, ICON_DIMENSION))
        self.selection_off = pygame.transform.smoothscale(pygame.image.load(ICONS.FOLDER + ICONS.SELECTION_OFF).convert_alpha(), (ICON_DIMENSION, ICON_DIMENSION))
        self.delete_on = pygame.transform.smoothscale(pygame.image.load(ICONS.FOLDER + ICONS.DELETE_ON).convert_alpha(), (ICON_DIMENSION, ICON_DIMENSION))
        self.delete_off = pygame.transform.smoothscale(pygame.image.load(ICONS.FOLDER + ICONS.DELETE_OFF).convert_alpha(), (ICON_DIMENSION, ICON_DIMENSION))
        self.rotate_left = pygame.transform.smoothscale(pygame.image.load(ICONS.FOLDER + ICONS.ROTATE_LEFT).convert_alpha(), (ICON_DIMENSION, ICON_DIMENSION))
        self.rotate_right = pygame.transform.smoothscale(pygame.image.load(ICONS.FOLDER + ICONS.ROTATE_RIGHT).convert_alpha(), (ICON_DIMENSION, ICON_DIMENSION))
        self.confirm_on = pygame.transform.smoothscale(pygame.image.load(ICONS.FOLDER + ICONS.CONFIRM_ON).convert_alpha(), (ICON_DIMENSION, ICON_DIMENSION))
        self.confirm_off = pygame.transform.smoothscale(pygame.image.load(ICONS.FOLDER + ICONS.CONFIRM_OFF).convert_alpha(), (ICON_DIMENSION, ICON_DIMENSION))


    def draw_title(self):
        self.current_buttons = []
        self.current_interactible_grid_cases = [[]]
        self.current_interactible_ships = []
        self.screen.fill(COLORS.OCEAN_COLOR_PRIMARY)

        # text
        self.draw_title_name(TEXTS.TITLE_PART_1, TEXTS.TITLE_PART_2)
        
        # ship
        ship_vertical_position = 2
        ship_width = 5
        ship_height = 15
        self.draw_title_ship(ship_vertical_position,ship_width,ship_height)
        
        # buttons
        btn_width = 4.8
        pvc_lines = []
        pvc_lines.append(TEXTS.TITLE_PVC_1)
        pvc_lines.append(TEXTS.TITLE_PVC_2)
        pvc_lines.append(TEXTS.TITLE_PVC_3)
        pvp_lines = []
        pvp_lines.append(TEXTS.TITLE_PVP_1)
        pvp_lines.append(TEXTS.TITLE_PVP_2)
        pvp_lines.append(TEXTS.TITLE_PVP_3)
        quit_lines = []
        quit_lines.append(TEXTS.TITLE_QUIT)
        pvc_vertical_position = ship_vertical_position + 2.1
        pvp_vertical_position = pvc_vertical_position + 5
        quit_vertical_position = pvp_vertical_position + 5
        
        self.draw_title_button(pvc_lines, pvc_vertical_position, btn_width, BUTTONS.TITLE_PVC)
        self.draw_title_button(pvp_lines, pvp_vertical_position, btn_width, BUTTONS.TITLE_PVP)
        self.draw_title_button(quit_lines, quit_vertical_position, btn_width, BUTTONS.TITLE_QUIT)

        pygame.display.flip() # updates the entire display

    def draw_placement(self, is_player_1, player, placement_mode):
        self.current_buttons = []
        self.current_interactible_grid_cases = [[]]
        self.current_interactible_ships = []
        self.screen.fill(COLORS.BACKGROUND_COLOR)
        
        is_select_mode = placement_mode == PLACEMENT_MODE.SELECTION

        # grid
        player_grid_position = Vector2(1,1)
        self.draw_grid(player_grid_position, True) # player's grid

        # ships
        self.draw_ships_on_grid(player_grid_position, player.ships, player.selected_ship, True) # player's ships

        # texts
        info_text = TEXTS.PLACEMENT_INFO
        info_pos = Vector2(2+GRID_SIZE, 2+GRID_SIZE)
        info_width = 12
        info_height = 2
        self.draw_text(info_text,info_pos,info_width,info_height,False,-1)

        info_player_text = TEXTS.PLACEMENT_PLAYER_B
        if is_player_1: info_player_text = TEXTS.PLACEMENT_PLAYER_A
        info_player_pos = Vector2(info_pos.x, info_pos.y+info_height+0.5)
        info_player_width = 3
        self.draw_text(info_player_text,info_player_pos,info_player_width,info_height,False,-1)

        # buttons
        btn_width = 3
        btn_height = 2
        btn_space_between = 0.5

        rotate_left_btn_icon = self.rotate_left
        select_btn_icon = self.selection_off
        rotate_right_btn_icon = self.rotate_right
        delete_btn_icon = self.delete_on
        if is_select_mode:
            select_btn_icon = self.selection_on
            delete_btn_icon = self.delete_off
        
        btn_pad_pos = Vector2(1, GRID_SIZE+2)
        rotate_left_btn_pos = btn_pad_pos
        select_btn_pos = Vector2(rotate_left_btn_pos.x+btn_width+btn_space_between, btn_pad_pos.y)
        rotate_right_btn_pos = Vector2(select_btn_pos.x+btn_width+btn_space_between, btn_pad_pos.y)
        delete_btn_pos = Vector2(select_btn_pos.x, select_btn_pos.y+btn_height+btn_space_between)

        self.draw_icon(rotate_left_btn_icon,rotate_left_btn_pos,btn_width,btn_height,False,BUTTONS.PLACEMENT_ROTATE_LEFT)
        self.draw_icon(select_btn_icon,select_btn_pos,btn_width,btn_height,is_select_mode,BUTTONS.PLACEMENT_SELECTION)
        self.draw_icon(rotate_right_btn_icon,rotate_right_btn_pos,btn_width,btn_height,False,BUTTONS.PLACEMENT_ROTATE_RIGHT)
        self.draw_icon(delete_btn_icon,delete_btn_pos,btn_width,btn_height,not is_select_mode,BUTTONS.PLACEMENT_DELETION)

        confirm_btn_icon = self.confirm_off
        all_ships_placed = True
        for ship in player.ships:
            if ship.position.x < 0 or ship.position.y < 0:
                all_ships_placed = False
                break
        if all_ships_placed: confirm_btn_icon = self.confirm_on
        confirm_btn_pos = Vector2(info_pos.x+info_width-btn_width, info_player_pos.y)
        self.draw_icon(confirm_btn_icon,confirm_btn_pos,btn_width,btn_height,all_ships_placed,BUTTONS.PLACEMENT_CONTINUE)

        # placement board
        placement_board_pos = Vector2(2+GRID_SIZE, 1)
        placement_board_width = 12
        placement_board_height = GRID_SIZE
        self.draw_ship_placement_board(player.ships,placement_board_pos,placement_board_width,placement_board_height,player.selected_ship)

        pygame.display.flip() # updates the entire display

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
        self.draw_ships_on_grid(player_grid_position, player.ships, -1, False) # player's ships


        # cases' state
        self.draw_grid_states(player_grid_position, player.board.grid, Vector2(-1,-1)) # where player launched
        self.draw_grid_states(opponent_grid_position, opponent.board.grid, player.selected_case) # where opponent launched

        # texts
        turn_text = TEXTS.GAME_PLAYER_ROUND_1 + str(turn)
        turn_text_position = Vector2(player_grid_position.x-1,1)
        turn_text_width = opponent_grid_position.x + GRID_SIZE
        turn_text_height = 1
        if is_player_1 : turn_text += TEXTS.GAME_PLAYER_ROUND_2A
        else : turn_text += TEXTS.GAME_PLAYER_ROUND_2B
        self.draw_text(turn_text, turn_text_position, turn_text_width, turn_text_height, False, -1) # "tour x du joueur y"


        grid_text_width = GRID_SIZE
        grid_text_height = 1  

        player_grid_text = TEXTS.GAME_PLAYER_TERRAIN
        opponent_grid_text = TEXTS.GAME_OPPONENT_TERRAIN
        player_grid_text_position = Vector2(player_grid_position.x, player_grid_position.y -1)
        opponent_grid_text_position = Vector2(opponent_grid_position.x, opponent_grid_position.y -1)
        self.draw_text(player_grid_text, player_grid_text_position, grid_text_width, grid_text_height, False, -1) # "votre terrain"
        self.draw_text(opponent_grid_text, opponent_grid_text_position, grid_text_width, grid_text_height, False, -1) # "terrain enemie"


        info_text_width = GRID_SIZE
        info_text_height = 1

        info_ship_text = TEXTS.GAME_OPPONENT_SHIPS_LEFT + str(opponent.nb_ship_unsunk())
        info_ship_text_position = Vector2(player_grid_position.x, player_grid_position.y + GRID_SIZE + 0.5)
        self.draw_text(info_ship_text, info_ship_text_position, info_text_width, info_text_height, False, -1) # "navires enemie restant : z"

        info_shot_text = ""
        if opponent.nb_ship_unsunk() <= 0: info_shot_text = TEXTS.GAME_SHOT_INFO_WON
        elif has_shot_left: info_shot_text = TEXTS.GAME_SHOT_INFO_CAN_SHOOT
        else: info_shot_text = TEXTS.GAME_SHOT_INFO_CANNOT_SHOOT
        info_shot_text_position = Vector2(info_ship_text_position.x, info_ship_text_position.y + info_text_height +0.5) # texts with shot info
        self.draw_text(info_shot_text, info_shot_text_position, info_text_width, info_text_height, False, -1)
        
        # button
        btn_height = 2

        end_turn_text = ""
        if has_shot_left and opponent.nb_ship_unsunk() != 0: end_turn_text = TEXTS.GAME_END_TURN_UNAVAILABLE
        else: end_turn_text = TEXTS.GAME_END_TURN_AVAILABLE
        end_turn_text_width = 5
        end_turn_text_position = Vector2(opponent_grid_position.x + GRID_SIZE - end_turn_text_width, opponent_grid_position.y + GRID_SIZE +1)
        self.draw_text(end_turn_text, end_turn_text_position, end_turn_text_width, btn_height, True, BUTTONS.GAME_CONTINUE) # "Terminer le tour"

        # button with icon

        shoot_icon = self.launch_off
        if has_shot_left: shoot_icon = self.launch_on
        shoot_width = 3
        shoot_position = Vector2(opponent_grid_position.x, opponent_grid_position.y + GRID_SIZE + 1)
        self.draw_icon(shoot_icon, shoot_position, shoot_width, btn_height, False, BUTTONS.GAME_LAUNCH) # "shoot" button

        pygame.display.flip() # updates the entire display

    def draw_transition(self, is_player_2_next):
        self.current_buttons = []
        self.current_interactible_grid_cases = [[]]
        self.current_interactible_ships = []
        self.screen.fill(COLORS.BACKGROUND_COLOR)
        self.draw_transition_background()

        # text
        text = TEXTS.TRANSITION_PASS_KEYBOARD_TO
        if is_player_2_next: text += TEXTS.TRANSITION_PLAYER_B
        else: text += TEXTS.TRANSITION_PLAYER_A
        pos = Vector2(3,2)
        width = 19
        height = 3
        self.draw_text(text, pos, width, height, False, -1)

        # button
        btn_width = 5
        btn_height = 2
        btn_position = Vector2(10,13)
        lines = []
        lines.append(TEXTS.TRANSITION_CONTINUE)
        if is_player_2_next: lines.append(TEXTS.TRANSITION_PLAYER_B)
        else: lines.append(TEXTS.TRANSITION_PLAYER_A)
        self.draw_transition_button(lines,btn_position,btn_width,btn_height, BUTTONS.TRANSITION_CONTINUE)


        pygame.display.flip() # updates the entire display


    def draw_ai(self, turn, human_player, ai):
        self.current_buttons = []
        self.current_interactible_grid_cases = [[]]
        self.current_interactible_ships = []
        self.screen.fill(COLORS.BACKGROUND_COLOR)

        # grids
        player_grid_position = Vector2(2,5)
        self.draw_grid(player_grid_position, False) # player's grid

        # AI logs
        ai_logs_position = Vector2(4+GRID_SIZE, player_grid_position.y)
        ai_logs_width = GRID_SIZE
        ai_logs_height = GRID_SIZE
        self.draw_logs(ai.logs, ai_logs_position, ai_logs_width, ai_logs_height)

        # ships
        self.draw_ships_on_grid(player_grid_position, human_player.ships, -1, False) # player's ships

        # cases' state
        self.draw_grid_states(player_grid_position, human_player.board.grid, Vector2(-1,-1)) # player's grid state

        # texts
        turn_text = TEXTS.AI_ROUND_1 + str(turn) + TEXTS.AI_ROUND_2
        turn_text_position = Vector2(player_grid_position.x-1,1)
        turn_text_width = ai_logs_position.x + GRID_SIZE
        turn_text_height = 1

        self.draw_text(turn_text, turn_text_position, turn_text_width, turn_text_height, False, -1) # "tour x du de l'IA"


        grid_text_width = GRID_SIZE
        grid_text_height = 1  

        player_grid_text = TEXTS.AI_PLAYER_TERRAIN
        opponent_grid_text = TEXTS.AI_LOGS_HEADER
        player_grid_text_position = Vector2(player_grid_position.x, player_grid_position.y -1)
        opponent_grid_text_position = Vector2(ai_logs_position.x, ai_logs_position.y -1)
        self.draw_text(player_grid_text, player_grid_text_position, grid_text_width, grid_text_height, False, -1) # "votre terrain"
        self.draw_text(opponent_grid_text, opponent_grid_text_position, grid_text_width, grid_text_height, False, -1) # "terrain enemie"
        
        # button
        btn_height = 2

        end_ai_turn_text = "" #TODO: DEFINE CONDITION TO ALLOW TO CONTINUE, LEFT AS 'TRUE' AS PLACEHOLDER
        if True : end_ai_turn_text = TEXTS.AI_CONTINUE
        else: end_ai_turn_text = TEXTS.AI_WAIT
        end_turn_text_width = 5
        end_turn_text_position = Vector2(ai_logs_position.x + GRID_SIZE - end_turn_text_width, ai_logs_position.y + GRID_SIZE +1)
        self.draw_text(end_ai_turn_text, end_turn_text_position, end_turn_text_width, btn_height, True, BUTTONS.AI_CONTINUE) # "Terminer le tour"

        pygame.display.flip() # updates the entire display
        

    def draw_victory(self, player_1, player_2, gamemode):
        self.current_buttons = []
        self.current_interactible_grid_cases = [[]]
        self.current_interactible_ships = []
        self.screen.fill(COLORS.BACKGROUND_COLOR)

        # grids
        player_grid_position = Vector2(2,5)
        opponent_grid_position = Vector2(4+GRID_SIZE, 5)

        self.draw_grid(player_grid_position, False) # player's grid
        self.draw_grid(opponent_grid_position, False) # opponent's grid


        # ships
        self.draw_ships_on_grid(player_grid_position, player_1.ships, -1, False) # player's ships
        self.draw_ships_on_grid(opponent_grid_position, player_2.ships, -1, False) # opponent's ships

        # cases' state
        self.draw_grid_states(player_grid_position, player_1.board.grid, Vector2(-1,-1)) # player's grid state
        self.draw_grid_states(opponent_grid_position, player_2.board.grid, Vector2(-1,-1)) # opponent's grid state + aimed case

        # text
        victory_text = TEXTS.VICTORY_WINNER_1
        victory_text_position = Vector2(player_grid_position.x-1,1)
        victory_text_width = opponent_grid_position.x + GRID_SIZE
        victory_text_height = 2
        if player_1.nb_ship_unsunk() <= 0 : 
            if gamemode == GAMEMODE.PVC: victory_text += TEXTS.VICTORY_AI
            else: victory_text += TEXTS.VICTORY_PLAYER_B
        else : victory_text += TEXTS.VICTORY_PLAYER_A
        victory_text += TEXTS.VICTORY_WINNER_2
        self.draw_text(victory_text, victory_text_position, victory_text_width, victory_text_height, False, -1) # "Victoire de X"

        grid_text_width = GRID_SIZE
        grid_text_height = 1  

        player_grid_text = TEXTS.VICTORY_TERRAIN_OF + TEXTS.VICTORY_PLAYER_A
        opponent_grid_text = TEXTS.VICTORY_TERRAIN_OF
        if gamemode == GAMEMODE.PVC: opponent_grid_text += TEXTS.VICTORY_AI
        else: opponent_grid_text += TEXTS.VICTORY_PLAYER_B
        player_grid_text_position = Vector2(player_grid_position.x, player_grid_position.y -1)
        opponent_grid_text_position = Vector2(opponent_grid_position.x, opponent_grid_position.y -1)
        self.draw_text(player_grid_text, player_grid_text_position, grid_text_width, grid_text_height, False, -1) # "Terrain joueur 1"
        self.draw_text(opponent_grid_text, opponent_grid_text_position, grid_text_width, grid_text_height, False, -1) # "Terrain joueur 2/de l'IA"

        
        # button
        end_turn_text = TEXTS.VICTORY_CONTINUE
        end_turn_text_width = 5
        end_turn_height = 2
        end_turn_text_position = Vector2(opponent_grid_position.x + GRID_SIZE - end_turn_text_width, opponent_grid_position.y + GRID_SIZE +1)
        self.draw_text(end_turn_text, end_turn_text_position, end_turn_text_width, end_turn_height, True, BUTTONS.VICTORY_CONTINUE) # "Continuer"

        pygame.display.flip() # updates the entire display


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

    def draw_ships_on_grid(self, grid_position, ships, selected_ship, interactible): # ships on the grid are never interactible
        for variant in range(len(ships)):
            ship = ships[variant]
            if (ship.position.x >= 0 and ship.position.x < GRID_SIZE) and (ship.position.y >= 0 and ship.position.y < GRID_SIZE):
                position = Vector2(grid_position.x + ship.position.x, grid_position.y + ship.position.y)
                self.draw_ship(position, ship.length, ship.orientation, ship.sunk, interactible, variant == selected_ship, variant)

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

        if interactible:
            self.current_interactible_ships.append((ship_outline_rect,variant))

        pygame.draw.rect(self.screen,outline_color,ship_outline_rect)
        pygame.draw.rect(self.screen,inside_color,ship_inside_rect)

    def draw_grid_states(self, position, cases_state, selected_position): # also draws the selected case, if the selection is inside the grid
        for row in range(GRID_SIZE):
                for col in range(GRID_SIZE):
                    state_position = Vector2(position.x+row,position.y+col)
                    match cases_state[row][col]:
                        case CASE_STATE.MISS:
                            self.draw_miss_case_state(state_position)
                        case CASE_STATE.HIT:
                            self.draw_hit_case_state(state_position)
                        case CASE_STATE.SUNK:
                            self.draw_sunk_case_state(state_position)
                    if selected_position.x == row and selected_position.y == col and selected_position.x >= 0 and selected_position.y >= 0:
                        self.draw_selected_case(state_position)

    def draw_miss_case_state(self, position):
        color = COLORS.MISS_COLOR
        outline_thickness = 5
        outline_correction = 2
        center = ((position.x+0.5)*CASE_DIMENSION, (position.y+0.5)*CASE_DIMENSION)
        radius = CASE_DIMENSION/2 - outline_correction
        pygame.draw.circle(self.screen, color, center, radius, outline_thickness)

    def draw_hit_case_state(self, position):
        self.draw_cross(position, COLORS.HIT_COLOR)

    def draw_sunk_case_state(self, position):
        self.draw_cross(position, COLORS.SINKED_COLOR)

    def draw_cross(self, position, color):
        line_thickness = 5
        line_correction = 3
        line_1_start_position = (position.x*CASE_DIMENSION+line_correction, position.y*CASE_DIMENSION+line_correction)
        line_2_start_position = (position.x*CASE_DIMENSION+line_correction, (position.y+1)*CASE_DIMENSION-1-line_correction)
        line_1_end_position = ((position.x+1)*CASE_DIMENSION-1-line_correction, (position.y+1)*CASE_DIMENSION-1-line_correction)
        line_2_end_position = ((position.x+1)*CASE_DIMENSION-1-line_correction, position.y*CASE_DIMENSION+line_correction)
        pygame.draw.line(self.screen, color, line_1_start_position, line_1_end_position, line_thickness)
        pygame.draw.line(self.screen, color, line_2_start_position, line_2_end_position, line_thickness)

    def draw_selected_case(self, position):
        color = COLORS.SELECTED_COLOR
        outline_thickness = 5
        outline_correction = 2
        rect = pygame.Rect(position.x*CASE_DIMENSION+outline_correction, position.y*CASE_DIMENSION+outline_correction, CASE_DIMENSION-2*outline_correction, CASE_DIMENSION-2*outline_correction)
        pygame.draw.rect(self.screen, color, rect, outline_thickness, border_radius=1)

    def draw_icon(self, icon, position, dimension_x, dimension_y, selected, btn_id):
        background_rect = pygame.Rect(position.x*CASE_DIMENSION, position.y*CASE_DIMENSION, dimension_x*CASE_DIMENSION, dimension_y*CASE_DIMENSION)
        self.current_buttons.append((background_rect, btn_id))

        if selected:
            background_inside_rect = pygame.Rect(position.x*CASE_DIMENSION+5, position.y*CASE_DIMENSION+5, dimension_x*CASE_DIMENSION-10, dimension_y*CASE_DIMENSION-10)
            pygame.draw.rect(self.screen,COLORS.SELECTED_COLOR,background_rect)
            pygame.draw.rect(self.screen,COLORS.GRAPHIC_BACKGROUND_COLOR,background_inside_rect)
        else:
            pygame.draw.rect(self.screen,COLORS.GRAPHIC_BACKGROUND_COLOR,background_rect)

        icon_rect = icon.get_rect(center= ((position.x+(0.5*dimension_x))*CASE_DIMENSION, (position.y+(0.5*dimension_y))*CASE_DIMENSION))
        self.screen.blit(icon, icon_rect)

    def draw_text(self, text, position, dimension_x, dimension_y, interactible, btn_id): # text and buttons
        background_rect = pygame.Rect(position.x*CASE_DIMENSION, position.y*CASE_DIMENSION, dimension_x*CASE_DIMENSION, dimension_y*CASE_DIMENSION)
        if interactible:
            self.current_buttons.append((background_rect, btn_id))
        pygame.draw.rect(self.screen,COLORS.GRAPHIC_BACKGROUND_COLOR,background_rect)

        game_font = pygame.font.Font(TEXTS.FONT, 25)
        text_surface = game_font.render(text, True, COLORS.TEXT_COLOR)
        text_rect = text_surface.get_rect(center= ((position.x+(0.5*dimension_x))*CASE_DIMENSION, (position.y+(0.5*dimension_y))*CASE_DIMENSION))
        self.screen.blit(text_surface,text_rect)
    

    # complex elements that are only used in one screen respectively :

    def draw_logs(self, logs, position, dimension_x, dimension_y): # specific to AI logs
        background_rect = pygame.Rect(position.x*CASE_DIMENSION,position.y*CASE_DIMENSION,dimension_x*CASE_DIMENSION,dimension_y*CASE_DIMENSION)
        pygame.draw.rect(self.screen,COLORS.AI_LOGS_BACKGROUND_COLOR,background_rect)

        logs_font = pygame.font.Font(TEXTS.FONT, 20)

        #TODO IF LINE LENGTH > LINE LIMIT, SPLIT AT LIMIT

    def draw_ship_placement_board(self, ships, position, width, height, selected_ship):
        background_rect = pygame.Rect(position.x*CASE_DIMENSION,position.y*CASE_DIMENSION,width*CASE_DIMENSION,height*CASE_DIMENSION)
        pygame.draw.rect(self.screen,COLORS.GRAPHIC_BACKGROUND_COLOR,background_rect)

        game_font = pygame.font.Font(TEXTS.FONT, 25)
        initial_padding = 0.5
        between_ship_padding = 2
        side_padding = 0.3

        for ship_id in range(len(ships)):
            current_ship = ships[ship_id]
            selected = ship_id == selected_ship
            is_ship_posed = current_ship.position.x >= 0 and current_ship.position.y >= 0

            text_pos = Vector2((position.x+side_padding)*CASE_DIMENSION, (position.y+initial_padding+ship_id*between_ship_padding)*CASE_DIMENSION)
            ship_pos = Vector2(position.x+width-current_ship.length-side_padding, position.y+initial_padding+ship_id*between_ship_padding)

            text_surface = game_font.render(current_ship.name, True, COLORS.TEXT_COLOR)
            text_rect = text_surface.get_rect(topleft= (text_pos.x,text_pos.y))
            
            self.draw_ship(ship_pos, current_ship.length, ORIENTATION.HORIZONTAL, is_ship_posed, True, selected, ship_id)

            self.screen.blit(text_surface,text_rect)
        

    def draw_transition_background(self):
        ocean_width = GRID_SIZE*2
        ocean_height = GRID_SIZE*2
        while ocean_width*CASE_DIMENSION < SCREEN_WIDTH: ocean_width +=1
        while ocean_height*CASE_DIMENSION < SCREEN_HEIGHT: ocean_height += 1

        for row in range(ocean_height):
            if row % 2 == 0:
                for col in range(ocean_width):
                    rect = pygame.Rect(col*CASE_DIMENSION, row*CASE_DIMENSION, CASE_DIMENSION, CASE_DIMENSION)
                    chosen_color = COLORS.OCEAN_COLOR_SECONDARY
                    if col % 2 == 0:
                        chosen_color = COLORS.OCEAN_COLOR_PRIMARY
                    pygame.draw.rect(self.screen,chosen_color,rect)

            else:
                for col in range(ocean_width):
                    rect = pygame.Rect(col*CASE_DIMENSION, row*CASE_DIMENSION, CASE_DIMENSION, CASE_DIMENSION)
                    chosen_color = COLORS.OCEAN_COLOR_PRIMARY
                    if col % 2 == 0:
                        chosen_color = COLORS.OCEAN_COLOR_SECONDARY
                    pygame.draw.rect(self.screen,chosen_color,rect)

    def draw_transition_button(self, lines, position, dimension_x, dimension_y, btn_id):
        background_rect = pygame.Rect(position.x*CASE_DIMENSION, position.y*CASE_DIMENSION, dimension_x*CASE_DIMENSION, dimension_y*CASE_DIMENSION)
        self.current_buttons.append((background_rect, btn_id))
        pygame.draw.rect(self.screen,COLORS.GRAPHIC_BACKGROUND_COLOR,background_rect)

        btn_font = pygame.font.Font(TEXTS.FONT, 20)
        line_height = 0.7
        for i in range(len(lines)):
            line = lines[i]
            text_surface = btn_font.render(line,True,COLORS.TEXT_COLOR)
            text_rect = text_surface.get_rect(center= ((position.x+(0.5*dimension_x))*CASE_DIMENSION, position.y*CASE_DIMENSION + (i*line_height)*CASE_DIMENSION +0.6*CASE_DIMENSION))
            self.screen.blit(text_surface,text_rect)

    def draw_title_name(self, title_1_text, title_2_text):
        title_font = pygame.font.Font(TEXTS.FONT, 80)
        title_1_pos = Vector2(1,2)
        title_2_pos = Vector2(25,2)
        title_1_surface = title_font.render(title_1_text,True,COLORS.TITLE_COLOR)
        title_2_surface = title_font.render(title_2_text,True,COLORS.TITLE_COLOR)
        title_1_rect = title_1_surface.get_rect(topleft= (title_1_pos.x*CASE_DIMENSION, title_1_pos.y*CASE_DIMENSION))
        title_2_rect = title_2_surface.get_rect(topright= (title_2_pos.x*CASE_DIMENSION, title_2_pos.y*CASE_DIMENSION))
        self.screen.blit(title_1_surface,title_1_rect)
        self.screen.blit(title_2_surface,title_2_rect)
    
    def draw_title_ship(self, vertical_start, width, height): # doesn't includes it's buttons
        
        # draw top triangle
        a=1 #TODO

        # draw middle rectangle
        a=1 #TODO

        # draw bottom triangle
        a=1 #TODO

    def draw_title_button(self, lines, vertical_position, width, btn_id):
        btn_font = pygame.font.Font(TEXTS.FONT, 40)
        top_left = Vector2(13*CASE_DIMENSION - (width*CASE_DIMENSION)/2, vertical_position*CASE_DIMENSION)
        line_height = 1.333

        background_rect = pygame.Rect(top_left.x, top_left.y, width*CASE_DIMENSION, line_height*len(lines)*CASE_DIMENSION)
        self.current_buttons.append((background_rect,btn_id))
        pygame.draw.rect(self.screen, COLORS.TITLE_BUTTON_COLOR, background_rect)

        for i in range(len(lines)):
            line = lines[i]
            text_surface = btn_font.render(line,True,COLORS.TITLE_COLOR)
            text_rect = text_surface.get_rect(center= (top_left.x+(width/2)*CASE_DIMENSION, top_left.y + (i*line_height)*CASE_DIMENSION +0.6*CASE_DIMENSION))
            self.screen.blit(text_surface,text_rect)