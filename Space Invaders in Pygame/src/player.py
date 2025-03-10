import pygame

from settings import settings


class Player(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('../graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=pos)
        self.speed = settings["player"]["speed"]

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect += self.speed
