import pygame
import sys
from setting import Setting
from ship import Ship
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
def keydown_event(event,ship,setting,screen,bullets,bigs):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = True
    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = True
    if event.key == pygame.K_UP or event.key == pygame.K_w:
        ship.moving_on = True
    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
        ship.moving_under = True
    if event.key == pygame.K_SPACE or event.key == pygame.K_j:
       shot_bullet(bullets,setting,screen,ship)
    if event.key == pygame.K_k:
        shot_big(bigs,setting,screen,ship)
        
def keyup_event(event,ship):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = False
    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = False
    if event.key == pygame.K_UP or event.key == pygame.K_w:
        ship.moving_on = False
    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
        ship.moving_under = False

def checkout_key(ship,setting,screen,bullets,bigs):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                keydown_event(event,ship,setting,screen,bullets,bigs)
            elif event.type == pygame.KEYUP:
                keyup_event(event,ship)

def update_screen(setting,screen,ship,bullets,bigs):
    screen.fill(setting.bg_color) #白色屏幕
    for bullet in bullets:
        bullet.draw_bullet() #画子弹
    for big in bigs:
        big.draw_big()
    ship.blitme() #画飞船 根据ship.rect
    pygame.display.update() #屏幕不断更新
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
    