import pygame

from settings import settings


class Laser(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((4, 20))
        self.image.fill('White')
        self.rect = self.image.get_rect(center=pos)
        self.speed = settings["laser"]["speed"]

    def destroy(self):
        if self.rect.y <= -50 or self.rect.y >= settings["screen"]["height"]:
            self.kill()

    def update(self):
        self.rect.y += self.speed
        self.destroy()
