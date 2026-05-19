# AUTEUR : LDM
# CREATION : 30.04.2026
# contain the logic related to the gameplay

from enum import Enum
from pygame import Vector2
from player import PLAYER
from ui import UI
from ai import AI
from constants import BUTTONS, GAMEMODE, PLACEMENT_MODE

class Stage(Enum): # Used to determine which screen to show
    TITLE = 0 # Title screen
    PLACEMENT = 1 # Placement screen
    GAME = 2 # Game screen, what you see when you think about "touché coulé"
    TRANSITION = 3 # Transition screen, skipped if in PVC
    VICTORY = 4 # End of game screen


    
class GAME:
    def __init__(self, surface):
        self.quit = False # Used by main.py to know if the user clicked on the "Quit game" button
        self.gamemode = GAMEMODE.PVP # Used to determine the 2nd opponent's type , defaults to PVP
        self.stage = Stage.TITLE # Current stage/screen of the game
        self.turn = 0 # Current turn of the game, 0 is the placement "turn"
        self.has_torpedo = False # Indicate if, during the GAME stage, can the current player shoot
        self.placement_mode = PLACEMENT_MODE.SELECTION # function of a click during the placement stage
        self.is_player_1_turn = True # Indicate if Player 1 is currently playing (True) or Player 2 (False)

        self.player_1 = PLAYER() # Player that always start first, always human player
        self.player_2 = PLAYER() # Second player, whose used by the IA in PVC
        self.ui = UI(surface) # UI of the game, also referred to as "IHM"
        self.ai = AI(self.player_2,self) # Behavior of the Computer player during PVC

    def ai_act(self): # Called to indicate the AI can make the next step (equivalant of a line in it's log)
        a=1 #TODO CALL AI AND TELL IT TO ACT

    def on_click(self, pos):
        match_found = False # used as multi-loop break
        # check order : buttons (interactible text+icon) then ships then cases, doesn't check after a match is found

        # buttons
        for (btn,btn_id) in self.ui.current_buttons:
            if btn.collidepoint(pos):
                self.handle_clicked_button(btn_id)
                match_found = True
            if match_found: break

        # ships
        for (ship,variant) in self.ui.current_interactible_ships:
            if ship.collidepoint(pos):
                self.handle_clicked_ship(variant)
                match_found = True
            if match_found: break

        # cases
        for row in range(len(self.ui.current_interactible_grid_cases)):
            for case in range(len(self.ui.current_interactible_grid_cases[row])):
                if self.ui.current_interactible_grid_cases[row][case].collidepoint(pos):
                    self.handle_clicked_case(row, case)
                    match_found = True
                if match_found: break
            if match_found: break

    def handle_clicked_button(self, btn_id):
        match self.stage:
            case Stage.TITLE:
                match btn_id:
                    case BUTTONS.TITLE_PVP:
                        self.start_pvp_match()
                    case BUTTONS.TITLE_PVC:
                        self.start_pvc_match()
                    case BUTTONS.TITLE_QUIT:
                        self.end_game()
            case Stage.PLACEMENT:
                match btn_id:
                    case BUTTONS.PLACEMENT_SELECTION:
                        self.set_placement_mode(False)
                    case BUTTONS.PLACEMENT_DELETION:
                        self.set_placement_mode(True)
                    case BUTTONS.PLACEMENT_ROTATE_LEFT:
                        self.rotate_ship(False)
                    case BUTTONS.PLACEMENT_ROTATE_RIGHT:
                        self.rotate_ship(True)
                    case BUTTONS.PLACEMENT_CONTINUE:
                        self.end_placement_turn()
            case Stage.GAME: # handles both game screen and AI screen
                match btn_id:
                    case BUTTONS.GAME_LAUNCH:
                        self.launch_missile()
                    case BUTTONS.GAME_CONTINUE:
                        self.player_end_their_turn()
                    case BUTTONS.AI_CONTINUE:
                        self.player_end_their_turn()
            case Stage.TRANSITION: # the transition stage only has one possible button, thus no need to check the btn_id
                self.pass_transition()
            case Stage.VICTORY: # the victory stage only has one possible button, thus no need to check the btn_id
                self.end_match()

    def handle_clicked_ship(self, variant): # since there is only one stage where ships are interactible, no need to check which stage we are in
        match self.placement_mode:
            case PLACEMENT_MODE.SELECTION: 
                self.select_ship(variant)
            case PLACEMENT_MODE.DELETION:
                self.delete_ship(variant)

    def handle_clicked_case(self, row, col):
         match self.stage:
            case Stage.PLACEMENT:
                self.place_ship(row,col)
            case Stage.GAME:
                self.aim_at_opponent(row,col)
        



    # buttons' actions

    def start_pvp_match(self):
        self.stage = Stage.PLACEMENT
        self.gamemode = GAMEMODE.PVP

    def start_pvc_match(self):
        self.stage = Stage.PLACEMENT
        self.gamemode = GAMEMODE.PVC

    def end_game(self):
        self.quit = True

    def set_placement_mode(self, is_deletion):
        if is_deletion: self.placement_mode = PLACEMENT_MODE.DELETION
        else: self.placement_mode = PLACEMENT_MODE.SELECTION

    def rotate_ship(self, to_the_right):
        concerned_player = self.player_2
        if self.is_player_1_turn: concerned_player = self.player_1
        concerned_player.rotate(to_the_right)

    def end_placement_turn(self):
        concerned_player = self.player_2
        if self.is_player_1_turn: concerned_player = self.player_1
    
        if self.are_all_ships_placed(concerned_player.ships):
            if self.is_player_1_turn:
                self.is_player_1_turn = False
                if self.gamemode == GAMEMODE.PVC:
                    a=1 #TODO: MAKE AI ACT HERE
            else:
                self.player_end_their_turn()

    def are_all_ships_placed(self, ships): #TODO: PASS THE RESULT OF THIS METHOD TO THE UI FOR THE PLACEMENT SCREEN
        all_ships_placed = True

        for ship in ships:
            if ship.position.x < 0 or ship.position.y < 0:
                all_ships_placed = False
        
        return all_ships_placed

    def launch_missile(self): # returns true if another shot is possible by the player (info needed by the AI class)
        concerned_player = self.player_2
        opponent = self.player_1
        if self.is_player_1_turn:
            concerned_player = self.player_1
            opponent = self.player_2

        if self.has_torpedo: # check that we have a valid target
            if concerned_player.launch(concerned_player.selected_case, opponent): # check if any ship has been hit
                return True
            else:
                self.has_torpedo = False
                return False

    def player_end_their_turn(self):
            if self.player_1.nb_ship_unsunk() <= 0 or self.player_2.nb_ship_unsunk() <= 0: # check if a player has won
                self.stage = Stage.VICTORY
            elif self.has_torpedo is False:
                if self.gamemode == GAMEMODE.PVP:
                    self.stage = Stage.TRANSITION
                else : 
                    self.stage = Stage.GAME

                if self.is_player_1_turn:
                    self.is_player_1_turn = False # pass to player 2
                else: 
                    self.is_player_1_turn = True # pass to player 1
                    self.turn +=1 # pass to next turn
                self.has_torpedo = True
                self.ai.clean_log()

    def pass_transition(self): # Called to end the transition between 2 players
        self.stage = Stage.GAME

    def end_match(self): # Called to return to title screen after the victory screen
        self.gamemode = GAMEMODE.PVP
        self.stage = Stage.TITLE
        self.turn = 0
        self.has_torpedo = False
        self.placement_mode = PLACEMENT_MODE.SELECTION
        self.is_player_1_turn = True

        self.player_1 = PLAYER() # Player that always start first, always human player
        self.player_2 = PLAYER() # Second player, whose used by the IA in PVC
        self.ai = AI(self.player_2) # Behavior of the Computer player during PVC


    # ship actions

    def select_ship(self,variant):
        concerned_player = self.player_2
        if self.is_player_1_turn: concerned_player = self.player_1
        concerned_player.select(variant)

    def delete_ship(self, variant):
        concerned_player = self.player_2
        if self.is_player_1_turn: concerned_player = self.player_1
        concerned_player.remove(variant)
    


    # case actions

    def place_ship(self, row, col):
        if self.placement_mode == PLACEMENT_MODE.SELECTION:
            concerned_player = self.player_2
            if self.is_player_1_turn: concerned_player = self.player_1
            concerned_player.place(Vector2(col,row))
    
    def aim_at_opponent(self, row, col):
        concerned_player = self.player_2
        opponent = self.player_1
        if self.is_player_1_turn: 
            concerned_player = self.player_1
            opponent = self.player_2
        return concerned_player.aim(Vector2(col,row), opponent) # return True if we have a valid target


    # UI

    def draw_everything(self): # Called to ask UI to draw the visuals
        match self.stage:
            case Stage.TITLE:
                self.ui.draw_title()
            case Stage.PLACEMENT:
                current_player = self.player_2
                if self.is_player_1_turn: current_player = self.player_1
                if self.gamemode == GAMEMODE.PVP:
                    self.ui.draw_placement(self.is_player_1_turn, current_player, self.placement_mode)
            case Stage.GAME:
                current_player = self.player_2
                opponent_player = self.player_1
                if self.is_player_1_turn:
                    current_player = self.player_1
                    opponent_player = self.player_2
                if self.gamemode == GAMEMODE.PVC and not self.is_player_1_turn:
                    self.ui.draw_ai(self.turn,current_player,self.ai)
                else:
                    self.ui.draw_game(self.is_player_1_turn,self.turn,self.has_torpedo,current_player,opponent_player)
            case Stage.TRANSITION:
                self.ui.draw_transition(not self.is_player_1_turn)
            case Stage.VICTORY:
                self.ui.draw_victory(self.player_1,self.player_2,self.gamemode)
