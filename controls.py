import pygame
import sys
from bullet import Bullet


def events(screen, gun, bullets):
    #обработка событий
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if key[pygame.K_d] and gun.rect.centerx < 660:
            #передвижение корабля вправо
            gun.rect.centerx += 5
        if key[pygame.K_a] and gun.rect.centerx > 40:
            #передвижение корабля влево
            gun.rect.centerx -= 5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)


def update(bg_color, screen, gun, ino, bullets):
    #обновление экрана
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    ino.draw()
    pygame.display.flip()


def update_bullet(bullets):
    #обновлять позиции пули
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
