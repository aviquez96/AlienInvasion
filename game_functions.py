import sys

import pygame

def check_events():
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

def update_screen(ai_settings, screen, ship):
    screen.fill(ai_settings.background_color)
        ship.blitme()

        #Refresh the most recently drawn screen
        pygame.display.flip()