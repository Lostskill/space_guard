import pygame
import controls
from gun import Gun
from pygame.sprite import Group
from alien import Alien
def run():

    pygame.init()
    screen = pygame.display.set_mode((1270 ,800))
    pygame.display.set_caption("Space Gurad")
    bg_color = (0,0,0)
    gun = Gun(screen)
    bullets = Group()
    aliens = Group()
    controls.create_army(screen,aliens)

    while True:
        controls.events(screen,gun, bullets)
        gun.update()
        #bullets.update()
        controls.update(bg_color, screen, gun,aliens, bullets)
        controls.update_bullets(bullets)

run()