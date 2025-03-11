import pygame

from settings import settings
from laser import Laser


class Player(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        # general
        self.image = pygame.image.load('../graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=pos)
        self.speed = settings["player"]["speed"]
        # shooting
        self.ready = True
        self.laser_time = 0
        self.laser_cooldown = settings["player"]["laser"]["cooldown"]
        # player lasers
        self.lasers = pygame.sprite.Group()

    def get_input(self):
        keys = pygame.key.get_pressed()

        # horizontal movement
        if keys[pygame.K_RIGHT] and self.rect.x < settings["screen"]["width"] - self.rect.width:
            self.rect.x += self.speed
        elif keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed

        if keys[pygame.K_SPACE] and self.ready:
            self.shoot_laser()
            # add cooldown time to recharge
            self.ready = False
            self.laser_time = pygame.time.get_ticks()

    def recharge(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if (current_time - self.laser_time) >= self.laser_cooldown:
                self.ready = True

    def shoot_laser(self):
        # Add laser to sprite group
        self.lasers.add(Laser(self.rect.center, settings["player"]["laser"]["speed"]))

    def update(self):
        self.get_input()
        self.recharge()
        self.lasers.update()
