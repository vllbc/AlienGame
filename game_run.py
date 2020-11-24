import pygame
import sys

from setting import Setting
from ship import Ship
from alien import Alien
from bullet import Bullet
from big_recruit import BigRecruit

def shot_bullet(bullets,setting,screen,ship):
    if len(bullets) < setting.bullet_limit: #屏幕上最多有3个子弹
        new_Bullet = Bullet(setting,screen,ship) 
        bullets.add(new_Bullet)
        
def shot_big(bigs,setting,screen,ship):
    if len(bigs) < setting.big_limit:
        new_big = BigRecruit(screen,ship,setting)
        bigs.add(new_big)
        
def keydown_event(event,ship,setting,screen,bullets,bigs,logger):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = True
        logger.debug("move right")
    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = True
        logger.debug("move left")
    if event.key == pygame.K_UP or event.key == pygame.K_w:
        ship.moving_on = True
        logger.debug("move up")
    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
        ship.moving_under = True
        logger.debug("move down")
    if event.key == pygame.K_SPACE or event.key == pygame.K_j:
       shot_bullet(bullets,setting,screen,ship)
       logger.debug("shot")
    if event.key == pygame.K_k:
        shot_big(bigs,setting,screen,ship)
        logger.debug("big!")
    if event.key == pygame.K_q:
        sys.exit()
        
def keyup_event(event,ship):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = False
    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = False
    if event.key == pygame.K_UP or event.key == pygame.K_w:
        ship.moving_on = False
    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
        ship.moving_under = False

def checkout_key(ship,setting,screen,bullets,bigs,logger):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                keydown_event(event,ship,setting,screen,bullets,bigs,logger)
            elif event.type == pygame.KEYUP:
                keyup_event(event,ship)
                
def update_bullets(bullets):
    bullets.update() #子弹更新 
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def update_big(bigs):
    bigs.update()
    for big in bigs.copy():
        if big.rect.bottom <= 0:
            bigs.remove(big)
            
def get_alien_num(setting,alien_width):
    avaiable_width = setting.width - 2*alien_width
    number_aliens = int(avaiable_width/(2*alien_width))
    return number_aliens

def create_aliens(setting,screen,aliens,alien_num,row_number):
    alien = Alien(screen,setting)
    alien_width = alien.rect.width
    alien.rect.x = alien_width+2*alien_width*alien_num
    alien.rect.y = alien.rect.height+2*alien.rect.height*row_number
    aliens.add(alien)
    
def create_fleet(setting,screen,aliens,ship):
    alien = Alien(screen,setting)
    numbers_aliens = get_alien_num(setting,alien.rect.width)
    numbers_rows = get_number_rows(setting,ship.rect.height,alien.rect.height)
    for row_number in range(numbers_rows):
        for alienw in range(numbers_aliens):
            create_aliens(setting,screen,aliens,alienw,row_number)

def get_number_rows(setting,ship_height,alien_height):
    avaiable = (setting.height-3*alien_height-ship_height)
    number_rows = int(avaiable/(2*alien_height))
    return number_rows
    
def check_edge(aliens,setting):
    for alien in aliens.sprites():
        if alien.check_edges():
            drop_from(aliens,setting)
            break

def drop_from(aliens,setting):
    for alien in aliens.sprites():
        alien.rect.y += setting.drop_speed
    setting.left_or_right *= -1


def update_aliens(aliens,setting):
    check_edge(aliens,setting)
    aliens.update()
def update_screen(setting,screen,ship,bullets,bigs,aliens):
    screen.fill(setting.bg_color) #白色屏幕
    for bullet in bullets:
        bullet.draw_bullet() #画子弹
    for big in bigs:
        big.draw_big()
    ship.blitme() #画飞船 根据ship.rect
    aliens.draw(screen)
    pygame.display.update() #屏幕不断更新