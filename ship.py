import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/ship.bmp')
        self.rectangle = self.image.get_rect()
        self.screen_rectangle = screen.get_rect()

        self.center = float(self.rectangle.centerx)

        self.moving_right = False
        self.moving_left = False

        self.rectangle.centerx = self.screen_rectangle.centerx
        self.rectangle.bottom = self.screen_rectangle.bottom

    def blitme(self):
        #draws the image at the position of rectangle
        self.screen.blit(self.image, self.rectangle)

    def update(self):
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor

        self.rectangle.centerx = self.center