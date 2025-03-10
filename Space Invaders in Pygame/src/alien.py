import pygame

from settings import settings


class Alien(pygame.sprite.Sprite):
    def __init__(self, color, x_cor, y_cor):
        super().__init__()
        self.image = pygame.image.load(settings["alien"]["color"][color]).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x_cor, y_cor))

    def update(self, direction):
        self.rect.x += direction
