import pygame

from settings import settings


class Alien(pygame.sprite.Sprite):
    def __init__(self, color, x_cor, y_cor):
        super().__init__()
        self.image = pygame.image.load(settings["alien"]["color"][color]).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x_cor, y_cor))

    def update(self, direction):
        self.rect.x += direction


class Extra(pygame.sprite.Sprite):
    def __init__(self, side, settings1=settings):
        super().__init__()
        self.image = pygame.image.load('../graphics/extra.png').convert_alpha()

        if side == "right":
            x = settings["screen"]["width"] + 50
            self.speed = -3
        else:
            x = -50
            self.speed = 3

        self.rect = self.image.get_rect(topleft=(x, 40))

    def update(self):
        self.rect.x += self.speed
