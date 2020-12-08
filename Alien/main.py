import pygame
import logging
from pygame.sprite import Group
from setting import Setting
from ship import Ship
from alien import Alien
from game_run import *
from big_recruit import BigRecruit
logging.basicConfig(level=logging.DEBUG,format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)
logger.debug("Start debug")
def main():
    pygame.init()
    game_Setting = Setting() #创建setting类
    logger.debug("create setting class")
    screen = pygame.display.set_mode((game_Setting.width,game_Setting.height)) #创建屏幕对
    logger.debug("create screen")
    game_Ship = Ship(screen,game_Setting)#创建飞船类
    logger.debug("create Ship class")
    bigs = Group()
    bullets = Group() #创建子弹k组
    aliens = Group()
    logger.debug("create bigs and bullets")
    pygame.display.set_caption("Tank") #题
    create_fleet(game_Setting,screen,aliens,game_Ship)
    while True:
        checkout_key(game_Ship,game_Setting,screen,bullets,bigs,logger) #检查键盘事件
        game_Ship.update() #飞船更新
        update_bullets(bullets)
        update_big(bigs)
        update_aliens(aliens,game_Setting)
        update_screen(game_Setting,screen,game_Ship,bullets,bigs,aliens) #屏幕更新
if __name__ == "__main__":
    main()
