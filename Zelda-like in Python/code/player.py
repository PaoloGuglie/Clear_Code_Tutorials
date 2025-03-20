import pygame

from settings import *
from support import import_folder


class Player(pygame.sprite.Sprite):
    def __init__(
            self,
            pos,
            groups,
            obstacle_sprites,
            create_attack,
            destroy_attack,
            create_magic
    ):
        super().__init__(groups)
        # get the player
        self.image = pygame.image.load('../graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -26)

        # player animations
        self.animations = None
        self.import_player_assets()
        self.status = 'down'
        self.frame_index = 0
        self.animation_speed = 0.15

        # Movement
        self.direction = pygame.math.Vector2()
        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = None
        self.create_attack = create_attack
        self.destroy_attack = destroy_attack

        # Obstacles
        self.obstacle_sprites = obstacle_sprites

        # Weapon
        self.weapon_index = 0
        self.weapon = list(weapon_data.keys())[self.weapon_index]
        self.can_switch_weapon = True
        self.weapon_switch_time = None

        self.switch_duration_cooldown = 200  # works with both weapon and magic

        # Magic
        self.create_magic = create_magic
        self.magic_index = 0
        self.magic = list(magic_data.keys())[self.magic_index]
        self.can_switch_magic = True
        self.magic_switch_time = None

        # Stats
        self.stats = {
                'health': 100,
                'energy': 60,
                'attack': 10,
                'magic': 4,
                'speed': 5
            }

        self.health = self.stats['health']
        self.energy = self.stats['energy']
        self.exp = 123
        self.speed = self.stats['speed']

    def import_player_assets(self):
        character_path = '../graphics/player/'
        self.animations = {
            'up': [],
            'down': [],
            'left': [],
            'right': [],
            'right_idle': [],
            'left_idle': [],
            'up_idle': [],
            'down_idle': [],
            'right_attack': [],
            'left_attack': [],
            'up_attack': [],
            'down_attack': []
        }

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def input(self):
        if not self.attacking:
            keys = pygame.key.get_pressed()

            # Movement input
            if keys[pygame.K_UP]:
                self.direction.y = -1
                self.status = 'up'
            elif keys[pygame.K_DOWN]:
                self.direction.y = 1
                self.status = 'down'
            else:
                self.direction.y = 0

            if keys[pygame.K_RIGHT]:
                self.direction.x = 1
                self.status = 'right'
            elif keys[pygame.K_LEFT]:
                self.direction.x = -1
                self.status = 'left'
            else:
                self.direction.x = 0

            # Attack input
            if keys[pygame.K_SPACE]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                self.create_attack()

            # Magic input
            if keys[pygame.K_RETURN]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                # magic
                style = list(magic_data.keys())[self.magic_index]
                strength = list(magic_data.values())[self.magic_index]['strength'] + self.stats['magic']
                cost = list(magic_data.values())[self.magic_index]['cost']
                self.create_magic(style, strength, cost)

            # Switch weapon input
            if keys[pygame.K_q] and self.can_switch_weapon:
                self.can_switch_weapon = False
                self.weapon_switch_time = pygame.time.get_ticks()
                self.weapon_index = (self.weapon_index + 1) % len(weapon_data)
                self.weapon = list(weapon_data.keys())[self.weapon_index]

            # Switch magic input
            if keys[pygame.K_e] and self.can_switch_magic:
                self.can_switch_magic = False
                self.magic_switch_time = pygame.time.get_ticks()
                self.magic_index = (self.magic_index + 1) % len(magic_data)
                self.magic = list(magic_data.keys())[self.magic_index]

    def get_status(self):

        # Idle status
        if (
            self.direction == (0, 0)
            and 'idle' not in self.status
            and 'attack' not in self.status
        ):
            self.status += '_idle'

        # Attack status
        if (
            self.attacking
            and 'attack' not in self.status
        ):
            self.direction.x = 0
            self.direction.y = 0

            if 'idle' in self.status:
                self.status = self.status.replace('_idle', '_attack')
            else:
                self.status += '_attack'

        elif 'attack' in self.status and not self.attacking:
            self.status = self.status.replace('_attack', '')

    def move(self, speed):

        # normalize the speed to avoid being faster in diagonal movement
        # compared to straight movement
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        # move the player's hitbox
        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        # place the rect where the hitbox is
        self.rect.center = self.hitbox.center

    def collision(self, direction):
        """ Check collisions with obstacle sprites """

        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:  # moving right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:  # moving left
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:  # moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:  # moving up
                        self.hitbox.top = sprite.hitbox.bottom

    def cooldowns(self):
        """ Timer for cooldown events """
        current_time = pygame.time.get_ticks()

        # Attack timer
        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False
                self.destroy_attack()

        # Weapon switch timer
        if not self.can_switch_weapon:
            if current_time - self.weapon_switch_time >= self.switch_duration_cooldown:
                self.can_switch_weapon = True

        # Magic switch timer
        if not self.can_switch_magic:
            if current_time - self.magic_switch_time >= self.switch_duration_cooldown:
                self.can_switch_magic = True

    def animate(self):
        animation = self.animations[self.status]

        # Loop over the frame index
        self.frame_index += self.animation_speed
        self.frame_index %= len(animation)

        # Set the image
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center=self.hitbox.center)

    def update(self):
        self.input()
        self.cooldowns()
        self.get_status()
        self.animate()
        self.move(self.speed)
