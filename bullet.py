import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self, ai_sett, screen, rocket):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, ai_sett.bullet_width, ai_sett.bullet_height)
        self.rect.centerx = rocket.rect.centerx
        self.rect.top = rocket.rect.top
        self.y = float(self.rect.y)
        self.color = ai_sett.bullet_color
        self.speed_factor = ai_sett.bullet_speed_f
    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)