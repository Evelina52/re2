import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)
    bullets = Group()
    bg_color = (230, 230, 230)
    while True:
        ship.update()
        gf.check_events(ai_settings, screen, ship, bullets)
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        pygame.display.flip()
run_game()
#echo $env:VIRTUAL_ENV для определения что код на виртуальной машине