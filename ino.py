import pygame
from pathlib import Path

class Ino(pygame.sprite.Sprite):
    #класс  одного пришельца
    
    def __init__(self, screen):
        #инициальзируем и задем начальную позицию
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(Path("./") / "Space-Wars" / "Models" / "vrag.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        #вывод пришельца на экран
        self.screen.blit(self.image, self.rect)

    def update(self):
        #перемещает пришельцев
        self.y += 0.1
        self.rect.y = self.y