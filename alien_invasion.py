import sys

import pygame
from settings import Settings
from ship import Ship

def run_game():
    #Initialize game and create screen object
    pygame.init()
    ai_settings = Settings();
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen);

    while True:
        #Keyboard event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(ai_settings.background_color)
        ship.blitme()

        #Refresh the most recently drawn screen
        pygame.display.flip()

run_game()