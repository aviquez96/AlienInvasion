import sys

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #Initialize game and create screen object
    pygame.init()
    ai_settings = Settings();
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen);
    bullets = Group()

    while True:
        #Keyboard event handler
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()

        #get rid of bullets that dissapeared
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()