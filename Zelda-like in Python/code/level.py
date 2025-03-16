import pygame

from settings import *
from tile import Tile
from player import Player
from debug import debug


class Level:
    def __init__(self):

        # get the display surface
        self.player = None
        self.display_surface = pygame.display.get_surface()

        # sprite groups setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        # sprite setup
        self.create_map()

    def create_map(self):

        # Items positions
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x_pos = col_index * TILESIZE
                y_pos = row_index * TILESIZE

                # Items sprites
                if col == 'x':
                    Tile((x_pos, y_pos), [self.visible_sprites, self.obstacle_sprites])
                elif col == 'p':
                    self.player = Player((x_pos, y_pos), [self.visible_sprites], self.obstacle_sprites)

    def run(self):
        # Update and draw the game
        self.visible_sprites.update()
        self.visible_sprites.draw(self.display_surface)
        debug(self.player.direction)
