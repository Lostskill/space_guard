import pygame,sys 
from bullet import Bullet
from alien import Alien
import time 

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


def update(bg_color, screen, stats, scorse, gun, aliens, bullets):
        screen.fill(bg_color)
        scorse.show_score()
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        gun.output()
        aliens.draw(screen)
        
        pygame.display.flip()

def update_bullets(screen,stats, scorse, bullets, aliens):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collision = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collision :
        for alienss in collision.values():
            stats.score += 10 * len(alienss)
        stats.score += 10
        scorse.image_score()
        check_high_score(stats, scorse)
        scorse.image_guns()
    if len(aliens) == 0:
        bullets.empty()
        create_army(screen,aliens)

def gunkill(stats,screen,score,gun,aliens,bullets):
    if stats.gunsleft > 0:
        stats.gunsleft -= 1
        score.image_guns()
        aliens.empty()
        bullets.empty()
        create_army(screen,aliens)
        gun.create_gun()
        time.sleep(1)
    else :
        stats.run_game = False
        sys.exit()
    

def update_aliens(stats,screen,score,gun,aliens,bullets):
    aliens.update()
    if pygame.sprite.spritecollideany(gun , aliens):
        gunkill(stats,screen,score,gun,aliens,bullets)
    aliens_check(stats,screen,score,gun,aliens,bullets)

def aliens_check(stats,screen,score,gun,aliens,bullets):
    screen_rect = screen.get_rect()
    for aliens in aliens.sprites():
        if aliens.rect.bottom >= screen_rect.bottom:
            gunkill(stats,screen,score,gun,aliens,bullets)
            break 

def create_army(screen, aliens):
    alien = Alien(screen)
    alien_width = alien.rect.width
    number_alien_x = int((1270 - 2 * alien_width) / alien_width)
    alien_height = alien.rect.height
    number_alien_y = int((800 - 100 - 2*alien_height) / alien_height)

    for row_number in range(number_alien_y - 1):
        for ino_number in range(number_alien_x):
            alien = Alien(screen)
            alien.x = alien_width + alien_width * ino_number
            alien.y = alien_height + alien_height * row_number
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height +  alien.rect.height * row_number
            aliens.add(alien) 


def check_high_score(stats, scorse):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        scorse.image_high_score()
        with open('highscore.text', 'w') as f :
            f.write(str(stats.high_score))