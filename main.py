import pygame
import controls
from gun import Gun
from pygame.sprite import Group
from pathlib import Path
from stats import Stats
from scores import Scores


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
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            bullets.update()
            controls.update(bg_color, screen, stats, sc, gun, inos, bullets)
            controls.update_bullet(screen, stats, sc, inos, bullets)
            controls.update_inos(stats, screen, sc, gun, inos, bullets)


run()