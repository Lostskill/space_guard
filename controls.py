import pygame,sys 
from bullet import Bullet
from alien import Alien

def events(screen,gun, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                gun.mright = True
            elif event.key == pygame.K_a:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen ,gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                gun.mright = False
            elif event.key == pygame.K_a:
                gun.mleft = False

def update(bg_color, screen, gun,aliens, bullets): 
        screen.fill(bg_color)
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        gun.output()
        aliens.draw()
        
        pygame.display.flip()

def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def create_army(screen, aliens):
    alien = Alien(screen)
    alien_width = alien.rect.width
    number_alien_x = int((800 - 2 * alien_width) / alien_width)

    for ino_number in range(number_alien_x):
        alien = Alien(screen)
        alien.x = alien_width + alien_width * ino_number
        alien.rect.x = alien.x