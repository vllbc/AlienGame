import pygame
from pygame.sprite import Group
from setting import Setting
from ship import Ship
from game_run import *
from big_recruit import BigRecruit
def main():
    pygame.init()
    game_Setting = Setting() #创建setting类
    screen = pygame.display.set_mode((game_Setting.width,game_Setting.height)) #创建屏幕对
    game_Ship = Ship(screen,game_Setting) #创建飞船类
    bigs = Group()
    bullets = Group() #创建子弹k组
    pygame.display.set_caption("Tank") #题
    while True:
        checkout_key(game_Ship,game_Setting,screen,bullets,bigs) #检查键盘事件
        game_Ship.update() #飞船更新
        update_bullets(bullets)
        update_big(bigs)
        update_screen(game_Setting,screen,game_Ship,bullets,bigs) #屏幕更新
if __name__ == "__main__":
    main()
