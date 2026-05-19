# AUTEUR : LDM
# CREATION : 30.04.2026
# Start of program and loop

import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from game import GAME

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()

AI_UPDATE = pygame.USEREVENT
pygame.time.set_timer(AI_UPDATE,2000)

game = GAME(screen)

while True:
    if game.quit:
        pygame.quit()
        sys.exit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Quitting the game (closing the window)
            pygame.quit()
            sys.exit()
        if event.type == AI_UPDATE: # tell game the AI can do another action (rythmed to not be instantaneous)
            game.ai_act()
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1: # activate on left-click release, to avoid missclicks
            game.on_click(event.pos)

    game.draw_everything()
    pygame.display.update()
    clock.tick(60)