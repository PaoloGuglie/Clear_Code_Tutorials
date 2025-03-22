import pygame

from entity import Entity
from settings import *
from support import *


class Enemy(Entity):
    def __init__(self, monster_name, pos, groups, obstacle_sprites):
        super().__init__(groups)

        # General setup
        self.animations = self.import_graphics(monster_name)
        self.sprite_type = 'enemy'

        # Graphics
        self.status = 'idle'
        self.image = self.animations[self.status][self.frame_index]

        # Movement
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)
        self.obstacle_sprites = obstacle_sprites

        # Stats
        self.monster_name = monster_name
        monster_info = monster_data[self.monster_name]
        self.health = monster_info['health']
        self.exp = monster_info['exp']
        self.speed = monster_info['speed']
        self.attack_damage = monster_info['damage']
        self.reststance = monster_info['resistance']
        self.attack_radius = monster_info['attack_radius']
        self.notice_radius = monster_info['notice_radius']
        self.attack_type = monster_info['attack_type']

        # Player interaction
        self.can_attack = True
        self.attack_time = None
        self.attack_cooldown = 400

    def get_player_distance_and_direction(self, player):

        # Get distance
        enemy_vector = pygame.math.Vector2(self.rect.center)
        player_vector = pygame.math.Vector2(player.rect.center)
        distance_vector = (player_vector - enemy_vector)
        distance = distance_vector.magnitude()

        # Get direction
        direction_vector = (player_vector - enemy_vector)
        if distance > 0:
            direction = direction_vector.normalize()
        else:
            direction = pygame.math.Vector2()

        return distance, direction

    def get_status(self, player):
        """ Set the correct status"""

        distance = self.get_player_distance_and_direction(player)[0]

        if distance <= self.attack_radius and self.can_attack:
            # reset animation
            if self.status != 'attack':
                self.frame_index = 0
            # set attack status
            self.status = 'attack'
        elif distance <= self.notice_radius:
            self.status = 'move'
        else:
            self.status = 'idle'

    def actions(self, player):
        """ Given the status, the enemies perform the correct action"""

        if self.status == 'attack':
            self.attack_time = pygame.time.get_ticks()
            print("attack")
        elif self.status == 'move':
            self.direction = self.get_player_distance_and_direction(player)[1]
        else:
            self.direction = pygame.math.Vector2()  # enemy not moving

    def import_graphics(self, name):
        self.animations = {
            'idle': [],
            'move': [],
            'attack': []
        }
        main_path = f'../graphics/monsters/{name}/'

        for animation in self.animations.keys():
            self.animations[animation] = import_folder(main_path + animation)

        return self.animations

    def animate(self):
        animation = self.animations[self.status]

        # Loop over the frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            if self.status == 'attack':
                self.can_attack = False
            self.frame_index = 0

        # Set the image
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center=self.hitbox.center)

    def cooldown(self):
        if not self.can_attack:
            current_time = pygame.time.get_ticks()
            if current_time - self.attack_time >= self.attack_cooldown:
                self.can_attack = True

    def update(self):
        self.move(self.speed)
        self.animate()
        self.cooldown()

    def enemy_update(self, player):
        self.get_status(player)
        self.actions(player)
