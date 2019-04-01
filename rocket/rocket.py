import pygame
from rocket_class import Rocket
import game_function as g_f
def run_game():
    pygame.init()
    screen=pygame.display.set_mode((800,400))
    pygame.display.set_caption("Rocket")
    rocket=Rocket(screen)
    while True:
        rocket.update()
        screen.fill((233,233,233))
        rocket.bltime()
        g_f.check_events(rocket)
        pygame.display.flip()
run_game()
