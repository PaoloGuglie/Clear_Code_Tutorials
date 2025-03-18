import pygame

from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *


class Level:
    def __init__(self):

        # get the display surface
        self.player = None
        self.display_surface = pygame.display.get_surface()

        # sprite groups setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        # sprite setup
        self.create_map_new()

    def create_map(self):  # DEPRECATED FUNCTION
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

    def create_map_new(self):
        layouts = {
            'boundary': import_csv_layout('../map/map_FloorBlocks.csv')
        }

        # Loop through the dictionary
        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x_pos = col_index * TILESIZE
                        y_pos = row_index * TILESIZE
                        # Place boundaries
                        if style == 'boundary':
                            Tile((x_pos, y_pos), [self.obstacle_sprites], 'invisible')

        self.player = Player((2000, 1400), [self.visible_sprites], self.obstacle_sprites)

    def run(self):
        # Update and draw the game
        self.visible_sprites.update()
        self.visible_sprites.custom_draw(self.player)


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

        # Setup
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_width() // 2
        self.half_height = self.display_surface.get_height() // 2
        self.offset = pygame.math.Vector2()  # offset for camera centering

        # Floor
        self.floor_surface = pygame.image.load('../graphics/tilemap/ground.png').convert()
        self.floor_rect = self.floor_surface.get_rect(topleft=(0, 0))

    def custom_draw(self, player):
        # get the player offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # Draw the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surface, floor_offset_pos)

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            # get the offset position for each element
            offset_pos = sprite.rect.topleft - self.offset
            # draw it to the screen
            self.display_surface.blit(sprite.image, offset_pos)
