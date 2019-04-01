import pygame
from settings import Settings
from ship import Ship
import game_function as g_f
# from forsen import Forsen
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
def run_game():
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien invasion")
    ship=Ship(ai_settings,screen)
    bullets=Group()
    aliens=Group()
    stats=GameStats(ai_settings)
    scoreboard=Scoreboard(ai_settings,screen,stats)
    play_button=Button(ai_settings,screen,"Play")
    #forsen=Forsen(screen)
    "Creating fleet of aliens"
    g_f.create_fleet(ai_settings,screen,ship,aliens)
    while True:
        g_f.check_events(ai_settings,screen,stats,scoreboard,play_button,ship,aliens,bullets)
        g_f.update_screen(ai_settings,screen,stats,scoreboard,ship,aliens,bullets,play_button)
        if stats.game_active:
                ship.update()
                bullets.update()
                g_f.update_bullets(ai_settings,screen,stats,scoreboard,ship,aliens,bullets)
                g_f.update_aliens(ai_settings,stats,screen,scoreboard,aliens,ship,bullets)
                
        #Task g_f.update_screen(ai_settings,screen,forsen)  
run_game()