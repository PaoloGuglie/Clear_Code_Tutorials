import pygame
import sys
from random import choice, randint

from settings import *
from tile import Tile
from player import Player
from enemy import Enemy
from weapon import Weapon
from ui import UI
from particles import AnimationPlayer
from magic import MagicPlayer
from support import *

from debug import debug


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
        self.attack_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()

        # sprite setup
        self.create_map_new()

        # User interface
        self.ui = UI()

        # Particles
        self.animation_player = AnimationPlayer()
        self.magic_player = MagicPlayer(self.animation_player)

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
            'object': import_csv_layout('../map/map_LargeObjects.csv'),
            'entities': import_csv_layout('../map/map_Entities.csv')
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
                            Tile((x_pos, y_pos),
                                 [self.visible_sprites, self.obstacle_sprites, self.attackable_sprites],
                                 'grass',
                                 random_grass_image)

                        if style == 'object':  # (using images IDs)
                            object_surface = graphics['objects'][int(col)]
                            Tile((x_pos, y_pos), [self.visible_sprites, self.obstacle_sprites], 'object', object_surface)

                        if style == 'entities':

                            # Player
                            if col == '394':
                                self.player = Player(
                                    (x_pos, y_pos),
                                    [self.visible_sprites],
                                    self.obstacle_sprites,
                                    self.create_attack,
                                    self.destroy_attack,
                                    self.create_magic)

                            # Enemies
                            else:
                                if col == '390':
                                    monster_name = 'bamboo'
                                elif col == '391':
                                    monster_name = 'spirit'
                                elif col == '392':
                                    monster_name = 'raccoon'
                                else:
                                    monster_name = 'squid'

                                Enemy(
                                    monster_name,
                                    (x_pos, y_pos),
                                    [self.visible_sprites, self.attackable_sprites],
                                    self.obstacle_sprites,
                                    self.damage_player,
                                    self.trigger_death_particles,
                                    self.add_exp)

    def create_attack(self):
        """ Weapon has to be available inside the level.py file to be able
        to interact with enemies, grass..."""
        self.current_attack = Weapon(
            self.player,
            [self.visible_sprites, self.attack_sprites])

    def create_magic(self, style, strength, cost):

        if style == 'heal':
            self.magic_player.heal(self.player, strength, cost, [self.visible_sprites])

        elif style == 'flame':
            self.magic_player.flame(
                self.player,
                cost,
                [self.visible_sprites, self.attack_sprites])

    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()

        self.current_attack = None

    def player_attack_logic(self):
        if self.attack_sprites:
            # check for collisions
            for attack_sprite in self.attack_sprites:
                collision_sprites = pygame.sprite.spritecollide(attack_sprite, self.attackable_sprites, False)
                # operate on collided objects
                if collision_sprites:
                    for target_sprite in collision_sprites:
                        # grass collision
                        if target_sprite.sprite_type == 'grass':
                            pos = target_sprite.rect.center - pygame.math.Vector2(0, 50)
                            for leaf in range(randint(3, 6)):
                                self.animation_player.create_grass_particles(pos, [self.visible_sprites])
                            target_sprite.kill()
                        # enemy collision
                        elif target_sprite.sprite_type == 'enemy':
                            target_sprite.get_damage(self.player, attack_sprite.sprite_type)

    def check_player_death(self):
        """ Quit the game if the player's health reaches 0 """

        if self.player.health <= 0:
            quit_game()

    def damage_player(self, amount, attack_type):
        if self.player.vulnerable:
            self.player.health -= amount
            self.player.vulnerable = False
            self.player.hurt_time = pygame.time.get_ticks()
            # spawn particles
            self.animation_player.create_particles(
                attack_type,
                self.player.rect.center,
                [self.visible_sprites])
            # check player death
            self.check_player_death()

    def trigger_death_particles(self, pos, particle_type):
        self.animation_player.create_particles(particle_type, pos, self.visible_sprites)

    def add_exp(self, amount):
        self.player.exp += amount

    def run(self):
        # Update and draw the game
        self.visible_sprites.update()
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.enemy_update(self.player)
        self.player_attack_logic()
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

    def enemy_update(self, player):
        enemy_sprites = [i for i in self.sprites() if hasattr(i, 'sprite_type')
                         and i.sprite_type == 'enemy']

        for enemy in enemy_sprites:
            enemy.enemy_update(player)


def quit_game():
    pygame.quit()
    sys.exit()
