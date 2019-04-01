import pygame

class Rocket():
    def __init__(self,screen):
        self.image=pygame.image.load("images/rocket.bmp")
        self.screen=screen
        self.object_rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()        
        self.object_rect.center=self.screen_rect.center
        self.moving_up=False
        self.moving_down=False
        self.moving_right=False
        self.moving_left=False
    def bltime(self):
        self.screen.blit(self.image,self.object_rect)
    def update(self):
        if self.moving_up and self.screen_rect.top<self.object_rect.top:
            self.object_rect.top-=1
        if self.moving_down and self.screen_rect.bottom>self.object_rect.bottom:
            self.object_rect.bottom+=1
        if self.moving_left and self.screen_rect.left<self.object_rect.left:
            self.object_rect.left-=1
        if self.moving_right and self.screen_rect.right>self.object_rect.right:
            self.object_rect.right+=1