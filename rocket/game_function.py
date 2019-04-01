import pygame
import sys

def check_events(ship):
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                ship.moving_up=True
            if event.key==pygame.K_DOWN:
                ship.moving_down=True
            if event.key==pygame.K_RIGHT:
                ship.moving_right=True
            if event.key==pygame.K_LEFT:
                ship.moving_left=True
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_UP:
                ship.moving_up=False
            if event.key==pygame.K_DOWN:
                ship.moving_down=False
            if event.key==pygame.K_LEFT:
                ship.moving_left=False
            if event.key==pygame.K_RIGHT:
                ship.moving_right=False