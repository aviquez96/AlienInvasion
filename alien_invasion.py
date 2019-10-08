import sys

import pygame

def run_game():
    #Initialize game and create screen object
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    background_color = (230,230,230)

    while True:
        #Keyboard event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(background_color)
        #Refresh the most recently drawn screen
        pygame.display.flip()

run_game()