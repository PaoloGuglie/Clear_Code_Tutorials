import pygame

from settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type, surface=pygame.Surface((TILESIZE, TILESIZE))):
        super().__init__(groups)
        # get the image
        self.sprite_type = sprite_type
        self.image = surface
        # create offset only for objects
        if sprite_type == 'object':
            self.rect = self.image.get_rect(topleft=(pos[0], pos[1] - TILESIZE))
        else:
            self.rect = self.image.get_rect(topleft=pos)
        # keep the center point in the same position, shrink height by 5px each side.
        self.hitbox = self.rect.inflate(0, -10)
