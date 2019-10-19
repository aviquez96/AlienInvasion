import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    # A class to represent a single alien in the fleet

    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #Start each alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the aliens exact position
        self.x = float(self.rect.x)

    def blitme(self):
        #draw the alien at its current location
        self.scree.blit(self.image, self.rect)