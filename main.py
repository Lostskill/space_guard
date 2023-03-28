import pygame
import controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scorse import Scores

def run():

    pygame.init()
    screen = pygame.display.set_mode((1270 ,800))
    pygame.display.set_caption("Space Gurad")
    bg_color = (0,0,0)
    gun = Gun(screen)
    bullets = Group()
    aliens = Group()
    controls.create_army(screen,aliens)
    stats = Stats()
    scorse = Scores(screen,stats)

    while True:
        controls.events(screen,gun, bullets)
        if stats.run_game:
            gun.update()
            controls.update(bg_color, screen,stats, scorse, gun,aliens, bullets)
            controls.update_bullets(screen,stats,scorse,bullets,aliens )
            controls.update_aliens(stats,screen,scorse,gun,aliens,bullets)

run()