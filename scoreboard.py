import pygame.font
from pygame.sprite import Group
from rocketbeck import RocketBeck
class Scoreboard():
    def __init__(self, ai_sett, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_sett = ai_sett
        self.stats = stats
        
        self.text_color = (225, 225, 225)
        self.font = pygame.font.SysFont(None, 48)
        
        self.prep_score()
        self.prep_record()
        self.prep_level()
        self.prep_rocket()
    def prep_score(self):
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_sett.bg_color)
        
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right -20
        self.score_rect.top = 20
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.record_img, self.record_rect)
        self.screen.blit(self.level_img, self.level_rect)
        self.rockets.draw(self.screen)
    def prep_record(self):
        record = int(round(self.stats.record, -1))
        record_str = "{:,}".format(record)
        self.record_img = self.font.render(record_str, True, self.text_color, self.ai_sett.bg_color)
        self.record_rect = self.record_img.get_rect()
        self.record_rect.centerx = self.screen_rect.centerx
        self.record_rect.top = self.score_rect.top
    def prep_level(self):
        self.level_img = self.font.render(str(self.stats.level), True, self.text_color, self.ai_sett.bg_color)
        self.level_rect = self.level_img.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
    def prep_rocket(self):
        self.rockets = Group()
        for rocket_num in range(self.stats.rocket_crush):
            rocket = RocketBeck(self.ai_sett, self.screen)
            rocket.rect.x = 10 + rocket_num * rocket.rect.width
            rocket.rect.y = 10
            self.rockets.add_internal(rocket)
    