import pygame
class Ship:
    def __init__(self,screen,setting):
        self.setting = setting
        self.screen = screen
        self.image = pygame.image.load('img/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.moving_on = False
        self.moving_under = False
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)
        
    def update(self):
        if self.moving_right:
            if self.rect.right < self.screen_rect.right:
                self.rect.centerx += self.setting.move_speed
            else:
                self.rect.centerx += 0
        elif self.moving_left:
            if self.rect.left > self.screen_rect.left:
                self.rect.centerx -= self.setting.move_speed
            else:
                self.rect.centerx += 0
        elif self.moving_on:
            if self.rect.top > self.screen_rect.top:
                self.rect.bottom -= self.setting.move_speed
            else:
                self.rect.top += 0
        elif self.moving_under:
            if self.rect.bottom <self.screen_rect.bottom:
                self.rect.bottom += self.setting.move_speed
            else:
                self.rect.bottom += 0