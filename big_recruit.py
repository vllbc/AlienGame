import pygame

class BigRecruit(pygame.sprite.Sprite):
    def __init__(self,screen,ship,setting):
        super(BigRecruit,self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0,0,setting.big_width,setting.big_height)

        self.rect.centerx = ship.rect.centerx
        self.rect.bottom = ship.rect.bottom
        self.y = float(self.rect.y)
        self.color = setting.big_color
    def update(self):
        self.y -= 0.1
        self.rect.y = self.y
    def draw_big(self):
        pygame.draw.rect(self.screen,self.color,self.rect)