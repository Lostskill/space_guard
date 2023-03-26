import pygame
import controls
from gun import Gun

def run():

    pygame.init()
    screen = pygame.display.set_mode((1270 ,800))
    pygame.display.set_caption("Space Gurad")
    bg_color = (0,0,0)
    gun = Gun(screen)

    while True:
        controls.events(gun)
        gun.update()
        screen.fill(bg_color)
        gun.output()
        pygame.display.flip()
        

run()