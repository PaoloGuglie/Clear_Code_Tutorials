import pygame
from random import randint

from settings import *


class MagicPlayer:
    def __init__(self, animation_player):
        self.animation_player = animation_player
        self.sounds = {
            'heal': pygame.mixer.Sound('../audio/heal.wav'),
            'flame': pygame.mixer.Sound('../audio/Fire.wav')
        }
        self.sounds['heal'].set_volume(0.5)
        self.sounds['flame'].set_volume(0.2)

    def heal(self, player, strength, cost, groups):

        # Check for energy level
        if player.energy >= cost:
            player.health += strength
            player.energy -= cost
            self.sounds['heal'].play()
            # avoid going over 100% health
            if player.health >= player.stats['health']:
                player.health = player.stats['health']

            # Particles
            self.animation_player.create_particles('aura', player.rect.center, groups)
            self.animation_player.create_particles('heal', player.rect.center, groups)

    def flame(self, player, cost, groups):

        # Check for energy level
        if player.energy >= cost:
            player.energy -= cost

            self.sounds['flame'].play()

            # Get the flames direction
            if player.status.split('_')[0] == 'right':
                direction = pygame.math.Vector2(1, 0)
            elif player.status.split('_')[0] == 'left':
                direction = pygame.math.Vector2(-1, 0)
            elif player.status.split('_')[0] == 'up':
                direction = pygame.math.Vector2(0, -1)
            else:
                direction = pygame.math.Vector2(0, 1)

            # Create flames
            for i in range(1, 6):
                # horizontal
                if direction.x:
                    offset_x = (direction.x * i) * TILESIZE
                    x_pos = player.rect.centerx + offset_x + randint(-TILESIZE // 3, TILESIZE // 3)
                    y_pos = player.rect.centery + randint(-TILESIZE // 3, TILESIZE // 3)
                    self.animation_player.create_particles('flame', (x_pos, y_pos), groups)
                # vertical
                else:
                    offset_y = (direction.y * i) * TILESIZE
                    x_pos = player.rect.centerx + randint(-TILESIZE // 3, TILESIZE // 3)
                    y_pos = player.rect.centery + offset_y + randint(-TILESIZE // 3, TILESIZE // 3)
                    self.animation_player.create_particles('flame', (x_pos, y_pos), groups)
