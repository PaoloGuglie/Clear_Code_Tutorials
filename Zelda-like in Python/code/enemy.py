import pygame

from entity import Entity
from settings import *


class Enemy(Entity):
    def __init__(self, moster_name, pos, groups):
        super().__init__(groups)

        # General setup
        self.sprite_type = 'enemy'

        # Graphics
        self.image = pygame.Surface((64, 64))
        self.rect = self.image.get_rect(topleft=pos)
