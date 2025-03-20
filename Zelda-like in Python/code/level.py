import pygame
from random import choice

from settings import *
from tile import Tile
from player import Player
from weapon import Weapon
from ui import UI
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

        # Attack sprites
        self.current_attack = None

        # sprite setup
        self.create_map_new()

        # User interface
        self.ui = UI()

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
            'boundary': import_csv_layout('../map/map_FloorBlocks.csv'),
            'grass': import_csv_layout('../map/map_Grass.csv'),
            'object': import_csv_layout('../map/map_LargeObjects.csv')
        }

        graphics = {
            'grass': import_folder('../graphics/grass'),
            'objects': import_folder('../graphics/objects')
        }

        # Loop through the dictionary
        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x_pos = col_index * TILESIZE
                        y_pos = row_index * TILESIZE

                        # Place items
                        if style == 'boundary':
                            Tile((x_pos, y_pos), [self.obstacle_sprites], 'invisible')

                        if style == 'grass':
                            random_grass_image = choice(graphics['grass'])
                            Tile((x_pos, y_pos), [self.visible_sprites, self.obstacle_sprites], 'grass', random_grass_image)

                        if style == 'object':  # (using images IDs)
                            object_surface = graphics['objects'][int(col)]
                            Tile((x_pos, y_pos), [self.visible_sprites, self.obstacle_sprites], 'object', object_surface)

        self.player = Player(
            (2000, 1400),
            [self.visible_sprites],
            self.obstacle_sprites,
            self.create_attack,
            self.destroy_attack
        )

    def create_attack(self):
        """ Weapon has to be available inside the level.py file to be able
        to interact with enemies, grass..."""
        self.current_attack = Weapon(self.player, [self.visible_sprites])

    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()

        self.current_attack = None

    def run(self):
        # Update and draw the game
        self.visible_sprites.update()
        self.visible_sprites.custom_draw(self.player)
        self.ui.display(self.player)


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
        """ Used to move the game camera """

        # Get the player offset
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
