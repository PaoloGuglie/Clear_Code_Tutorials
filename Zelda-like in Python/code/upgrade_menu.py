import pygame

from settings import *


class UpgradeMenu:
    def __init__(self, player):

        # General setup
        self.display_surface = pygame.display.get_surface()
        self.player = player
        self.attribute_number = len(player.stats)
        self.attribute_names = list(player.stats.keys())
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        # Selection system
        self.selection_index = 0
        self.selection_time = None
        self.selection_cooldown = 300
        self.can_move = True

    def input(self):
        keys = pygame.key.get_pressed()

        if self.can_move:

            if keys[pygame.K_RIGHT]:
                self.selection_index = (self.selection_index + 1) % self.attribute_number
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()

            elif keys[pygame.K_LEFT]:
                if self.selection_index > 0:
                    self.selection_index = self.selection_index - 1
                else:
                    self.selection_index = self.attribute_number - 1
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()

            if keys[pygame.K_SPACE]:
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
                print(self.selection_index)

    def cooldowns(self):
        """ Timers for menu """

        # Menu movement timer
        if not self.can_move:
            current_time = pygame.time.get_ticks()
            if current_time - self.selection_time >= self.selection_cooldown:
                self.can_move = True

    def display(self):
        self.input()
        self.cooldowns()
