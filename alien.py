import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """one alien in the army"""
    def __init__(self, ai_settings, screen):
        """init alien to start position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        """load alien image and set rect"""
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()
        """aliens start in the top left"""
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        """exact position of alien"""
        self.x = float(self.rect.x)

    def check_edges(self):
        """if alien is at the edge returns true"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right/left"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        """draw alien at position"""
        self.screen.blit(self.image, self.rect)


