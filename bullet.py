import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        #создаем пулю в позиции пушки
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.color = 5, 255, 0
        self.speed = 4.5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        #перемещение пули вверх
        self.y -= self.speed
        self.rect.y = self.y
        
    def draw_bullet(self):
        #рисуем на экране
        pygame.draw.rect(self.screen, self.color, self.rect)