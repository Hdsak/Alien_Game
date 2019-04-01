import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    """Класс для корабля"""
    def __init__(self,ai_settings,screen):
        """Инициализирует корабль и задает его начальное положение"""
        super().__init__()
        self.screen=screen
        """Загрузка изображения кораблся и отрисовка прямоугольника"""
        self.image=pygame.image.load('images/ship.bmp')
        self.screen_rect=screen.get_rect()
        self.rect=self.image.get_rect()
        """каждый новый корабль появляется у нижнего экрана"""
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        self.moving_right=False
        self.moving_left=False
        self.ai_settings=ai_settings
        self.center=float(self.rect.centerx)
    def center_ship(self):
        self.rect.center=self.screen_rect.centerx
    def bltime(self):
        """Printing the ship"""
        self.screen.blit(self.image,self.rect)
    def update(self):
        if self.moving_right and self.rect.right< self.screen_rect.right:
            self.center+=self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left> self.screen_rect.left:
            self.center-=self.ai_settings.ship_speed_factor
        self.rect.centerx=self.center