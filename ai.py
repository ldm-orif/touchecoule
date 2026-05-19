# AUTEUR : LDM
# CREATION : 30.04.2026
# Contains the computer opponent's data and logic

from enum import Enum
from constants import SHIP_PER_PLAYER, ORIENTATION, GRID_SIZE, IA_LOG_LINE_LIMIT, IA_LOG_CHARACTER_PER_LINE_LIMIT, AI_LOGS_TEXT, CASE_STATE
from random import randint
from pygame import Vector2

class Hit_direction(Enum):
    UNKNOWN = 0
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class AI:
    def __init__(self, player, game):
        self.player = player
        self.logs = []
        self.last_hit = Vector2(-1,-1) # last successful hit (put to [-1;-1] if has sunk)
        self.last_hit_direction = Hit_direction.UNKNOWN
        self.game = game
        self.turn_finished = False

    def add_log(self, text):
        if self.logs.__len__() >= IA_LOG_LINE_LIMIT: # if the number of maximum lines is about or is exceeded, remove the first one and escalade every line.
            self.logs.pop[0]
        fixed_text = text
        if text.__len__() > IA_LOG_CHARACTER_PER_LINE_LIMIT:
            fixed_text = text[:IA_LOG_CHARACTER_PER_LINE_LIMIT - 3] + "..."
        self.logs.append(fixed_text)

    def clean_log(self):
        self.logs.clear()

    def placement_behavior(self): #all done in one go, unlike the behavior during the turns
        placed = 0

        while placed < SHIP_PER_PLAYER:
            self.player.selected_ship = placed

            orientation = randint(0,1)
            if orientation < 1:
                orientation = ORIENTATION.HORIZONTAL
            else :
                orientation = ORIENTATION.VERTICAL

            position = Vector2(float(randint(0,GRID_SIZE-1)),float(randint(0,GRID_SIZE-1)))

            self.player.ships[self.player.selected_ship].orientation = orientation
            self.player.ships[self.player.selected_ship].position = position

            if not self.player.collides():
                placed+=1

        self.player.selected_ship = -1
        self.game.end_placement_turn()


    def turn_behavior(self, can_shoot, opponent):
        if not self.turn_finished: # AI only acts if it hasn't finished it's turn
            if can_shoot:
                if opponent.nb_ship_unsunk() <= 0: # check if opponent still has boats to sink
                    self.turn_finished = True
                    ai_logs_won = AI_LOGS_TEXT.END_1B
                    self.add_log(str(ai_logs_won))
                    ai_log_turn_done = AI_LOGS_TEXT.END_2
                    self.add_log(str(ai_log_turn_done))
                else:
                    last_shot = self.last_hit
                    aimed_case = self.get_random_valid_case(CASE_STATE.CLEAN,opponent)
                    new_dicrection = self.last_hit_direction
                    if self.last_hit.x < 0 and self.last_hit.y < 0 : # check if we must search for a hit case
                        case_found = False
                        direction = self.get_first_valid_direction(last_shot,CASE_STATE.CLEAN,opponent)
                        for row in range(opponent.board.dimension):
                            if case_found: break
                            for col in range(opponent.board.dimension):
                                if case_found: break
                                if opponent.board.grid[row][col] == CASE_STATE.HIT and not self.get_first_valid_direction(last_shot,CASE_STATE.CLEAN,opponent) == Hit_direction.UNKNOWN:
                                    last_shot = Vector2(row,col)
                                    case_found = True
                                    possible_direction = self.get_first_valid_direction(last_shot,CASE_STATE.HIT,opponent)
                                    if not possible_direction == Hit_direction.UNKNOWN:
                                        match possible_direction:
                                            case Hit_direction.UP:
                                                possible_case = Vector2(last_shot.x,last_shot.y+1)
                                                if self.is_case_valid(possible_case, CASE_STATE.CLEAN, opponent):
                                                    direction = Hit_direction.DOWN
                                            case Hit_direction.DOWN:
                                                possible_case = Vector2(last_shot.x,last_shot.y-1)
                                                if self.is_case_valid(possible_case, CASE_STATE.CLEAN, opponent):
                                                    direction = Hit_direction.UP
                                            case Hit_direction.LEFT:
                                                possible_case = Vector2(last_shot.x+1,last_shot.y)
                                                if self.is_case_valid(possible_case, CASE_STATE.CLEAN, opponent):
                                                    direction = Hit_direction.RIGHT
                                            case Hit_direction.RIGHT:
                                                possible_case = Vector2(last_shot.x-1,last_shot.y)
                                                if self.is_case_valid(possible_case, CASE_STATE.CLEAN, opponent):
                                                    direction = Hit_direction.LEFT
                        if case_found: # if a hit but unsunk case is found, check if the surrounding cases are valid targets
                            match direction:
                                case Hit_direction.UP:
                                    possible_case = Vector2(last_shot.x,last_shot.y-1)
                                    if self.is_case_valid(possible_case, CASE_STATE.CLEAN, opponent):
                                        aimed_case = possible_case
                                case Hit_direction.DOWN:
                                    possible_case = Vector2(last_shot.x,last_shot.y+1)
                                    if self.is_case_valid(possible_case, CASE_STATE.CLEAN, opponent):
                                        aimed_case = possible_case
                                case Hit_direction.LEFT:
                                    possible_case = Vector2(last_shot.x-1,last_shot.y)
                                    if self.is_case_valid(possible_case, CASE_STATE.CLEAN, opponent):
                                        aimed_case = possible_case
                                case Hit_direction.RIGHT:
                                    possible_case = Vector2(last_shot.x+1,last_shot.y)
                                    if self.is_case_valid(possible_case, CASE_STATE.CLEAN, opponent):
                                        aimed_case = possible_case
                    
                    else: # then if we know where we last hit, hit in the known direction
                        direction = self.last_hit_direction
                        if direction == Hit_direction.UNKNOWN: # if we don't know the ship's direction, aim at an adjaçant valid case
                           direction = self.get_first_valid_direction(last_shot, CASE_STATE.CLEAN, opponent)
                           new_dicrection = direction
                        match direction:
                            case Hit_direction.UP:
                                aimed_case = Vector2(last_shot.x,last_shot.y-1)
                            case Hit_direction.DOWN:
                                aimed_case = Vector2(last_shot.x,last_shot.y+1)
                            case Hit_direction.LEFT:
                                aimed_case = Vector2(last_shot.x-1,last_shot.y)
                            case Hit_direction.RIGHT:
                                aimed_case = Vector2(last_shot.x+1,last_shot.y)
                    
                    ai_log_aiming = str(AI_LOGS_TEXT.AIM) + str(AI_LOGS_TEXT.LINE) + str(aimed_case.x) + str(AI_LOGS_TEXT.COLUMN) + str(aimed_case.y)
                    self.add_log(str(ai_log_aiming))
                    self.player.selected_case = aimed_case
                    
                    nb_unsunk_before = opponent.nb_ship_unsunk()
                    hit = self.game.launch_missile()
                    nb_unsunk_after = opponent.nb_ship_unsunk()
                    if hit:
                        if nb_unsunk_before > nb_unsunk_after: # if there are more sunk ship than before, we have sunk one
                            ai_log_sunk = str(AI_LOGS_TEXT.SINK_1) + str(nb_unsunk_after) + str(AI_LOGS_TEXT.SINK_2)
                            self.add_log(str(ai_log_sunk))
                            self.last_hit = Vector2(-1,-1)
                            self.last_hit_direction = Hit_direction.UNKNOWN
                        else: # if the number of unsunk ship is the same, we "only" hit one
                            ai_log_hit = AI_LOGS_TEXT.HIT
                            self.add_log(str(ai_log_hit))
                            self.last_hit = aimed_case
                            self.last_hit_direction = new_dicrection

                    else: # if missed
                        ai_log_missed = AI_LOGS_TEXT.MISS
                        self.add_log(str(ai_log_missed))
                        self.last_hit_direction = Hit_direction.UNKNOWN

            else: # if can't shoot: end turn
                self.turn_finished = True
                ai_logs_turn = AI_LOGS_TEXT.END_1A
                self.add_log(str(ai_logs_turn))
                ai_log_turn_done = AI_LOGS_TEXT.END_2
                self.add_log(str(ai_log_turn_done))
        

    def get_random_valid_case(self, valid_state, opponent):
        while True:
            aimed_case = Vector2(randint(0,GRID_SIZE-1),randint(0,GRID_SIZE-1))
            if self.is_case_valid(aimed_case, valid_state, opponent):
                return aimed_case

    def get_first_valid_direction(self, case, valid_state, opponent):
        if self.is_case_valid(Vector2(case.x,case.y-1), valid_state, opponent): return Hit_direction.UP
        if self.is_case_valid(Vector2(case.x,case.y+1), valid_state, opponent): return Hit_direction.DOWN
        if self.is_case_valid(Vector2(case.x-1,case.y), valid_state, opponent): return Hit_direction.LEFT
        if self.is_case_valid(Vector2(case.x+1,case.y), valid_state, opponent): return Hit_direction.RIGHT
        return Hit_direction.UNKNOWN


    def is_case_valid(self, case, valid_state, opponent):
        valid_case = False
        if case.x < GRID_SIZE and case.x >= 0 and case.y < GRID_SIZE and case.y >= 0:
            if opponent.board.grid[int(case.x)][int(case.y)] == valid_state:
                valid_case = True
                self.selected_case = case
        return valid_case
