import pygame
import controls
from gun import Gun
from pygame.sprite import Group
from pathlib import Path


def run():
    icon = pygame.image.load(Path("./") / "Space-Wars" / "Models" / "icon.png")
    pygame.display.set_icon(icon)
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Cosmos security")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)

    while True:
        controls.events(screen, gun, bullets)
        gun.update_gun()
        bullets.update()
        controls.update(bg_color, screen, gun, inos, bullets)
        controls.update_bullet(inos, bullets)
        controls.update_inos(inos)


run()
