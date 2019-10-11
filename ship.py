import pygame

class Ship():

    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load('images/ship.bmp')
        self.rectangle = self.image.get_rect()
        self.screen_rectangle = screen.get_rect()

        self.moving_right = False

        self.rectangle.centerx = self.screen_rectangle.centerx
        self.rectangle.bottom = self.screen_rectangle.bottom

    def blitme(self):
        #draws the image at the position of rectangle
        self.screen.blit(self.image, self.rectangle)

    def update(self):
        if self.moving_right:
            self.rectangle.centerx += 1