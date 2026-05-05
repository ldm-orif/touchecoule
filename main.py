# AUTEUR : LDM
# CREATION : 30.04.2026
# Start of program and loop

import pygame,sys
from pygame.math import Vector2
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

#TODO DECLARE MAIN HERE

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # TODO LISTEN TO GAME: IF SOMEONE PRESS THE QUIT BUTTON ALSO ACTIVATE THIS
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            a=1 #TODO HERE TELL GAME TO UPDATE
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1: # activate on left-click release, to avoid missclicks
            print("clicked on " + str(event.pos)) #TODO HERE SENT THE event.pos TO GAME TO CHECK COLLIDEPOINTS (pos is [x.y] tuple)

    #TODO HERE TELL UI VIA GAME TO DRAW
    pygame.display.update()
    clock.tick(60)