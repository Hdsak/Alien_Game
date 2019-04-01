import pygame

class Forsen():
    def __init__(self,screen):
        self.image=pygame.image.load('images/b85.bmp')
        self.screen=screen
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.center=self.screen_rect.center
    def bltime(self):
        self.screen.blit(self.image,self.rect)