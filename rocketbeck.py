import pygame
from pygame.sprite import Sprite
class RocketBeck(Sprite):
    def __init__(self, ai_sett, screen):
        super(RocketBeck, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/Rocketbeck.png')
        self.rect = self.image.get_rect()
        self.screen_rect= screen.get_rect()
        self.ai_sett = ai_sett
        self.center = float(self.rect.centerx)
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_sett.rocket_speed_f
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.ai_sett.rocket_speed_f
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    def center_rocket(self):
        self.center = self.screen_rect.centerx