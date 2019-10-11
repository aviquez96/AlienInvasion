import sys

import pygame

def check_events(ship):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship.rectangle.centerx += 1
                elif event.key == pygame.K_LEFT:
                    ship.rectangle.centerx -= 1

def update_screen(ai_settings, screen, ship):
    screen.fill(ai_settings.background_color)
    ship.blitme()

    #Refresh the most recently drawn screen
    pygame.display.flip()