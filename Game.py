import pygame
import game_functions as gf
from pygame.sprite import Group
from Settings import Settings
from rocketbeck import RocketBeck
from game_stats import  GameStats
from button import Button
from scoreboard import Scoreboard
def run_game():
    pygame.init()
    ai_sett = Settings()
    screen = pygame.display.set_mode((ai_sett.screen_width, ai_sett.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(screen, "Play")
    stats = GameStats(ai_sett)
    sb = Scoreboard(ai_sett, screen, stats)
    rocket = RocketBeck(ai_sett, screen)
    bullets = Group()
    alinzes = Group()
    gf.create_fleet(ai_sett, screen, rocket, alinzes)
    while True:
        gf.check_events(ai_sett, screen, stats, sb, play_button, rocket, alinzes, bullets)
        if stats.game_active:
            rocket.update()
            gf.update_bullets(ai_sett, screen, stats, sb, rocket, alinzes, bullets)
            gf.update_alinz(ai_sett, stats, sb, screen, rocket,  alinzes, bullets)
            gf.update_s(ai_sett, screen, stats, sb, rocket, alinzes, bullets, play_button)
run_game()
