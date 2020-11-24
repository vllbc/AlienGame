import pygame
class Alien(pygame.sprite.Sprite):
    def __init__(self,screen,setting):
        super().__init__()
        self.screen = screen
        self.setting = setting 
        self.image = pygame.image.load("img/alien.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.x =  0
        self.rect.y = 0
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def update(self):
        self.rect.x += self.setting.alien_move_speed * self.setting.left_or_right
    def check_edges(self):
        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <=0:
            return True