import pygame

from settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type, surface=pygame.Surface((TILESIZE, TILESIZE))):
        super().__init__(groups)
        # get the rock
        self.sprite_type = sprite_type
        self.image = surface
        self.rect = self.image.get_rect(topleft=pos)
        # keep the center point in the same position, shrinks height by 5px each side.
        self.hitbox = self.rect.inflate(0, -10)
