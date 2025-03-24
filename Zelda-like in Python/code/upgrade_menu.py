import pygame

from settings import *


class UpgradeMenu:
    def __init__(self, player):

        # General setup
        self.display_surface = pygame.display.get_surface()
        self.player = player
        self.attribute_number = len(player.stats)
        self.attribute_names = list(player.stats.keys())
        self.max_values = list(player.max_stats.values())
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        # Items creation
        self.height = self.display_surface.get_height() * 0.8
        self.width = self.display_surface.get_width() // 6
        self.item_list = None
        self.create_items()

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

    def create_items(self):
        self.item_list = []

        for i in range(self.attribute_number):

            # Horizontal position
            full_width = self.display_surface.get_width()
            increment = full_width // self.attribute_number
            left = (i * increment) + (increment - self.width) // 2

            # Vertical position
            top = self.display_surface.get_height() * 0.1

            # Create the object
            item = Item(left, top, self.width, self.height, i, self.font)
            self.item_list.append(item)

    def display(self):
        self.input()
        self.cooldowns()

        # Upgrade windows
        for index, item in enumerate(self.item_list):
            # attributes
            name = self.attribute_names[index]
            value = self.player.get_value_by_index(index)
            max_value = self.max_values[index]
            cost = self.player.get_cost_by_index(index)
            # display
            item.display(
                self.display_surface,
                self.selection_index,
                name,
                value,
                max_value,
                cost)


class Item:
    def __init__(self, left, top, width, height, index, font):
        self.rect = pygame.Rect(left, top, width, height)
        self.index = index
        self.font = font

    def display_names(self, surface, name, cost, selected):

        # Title text
        title_surface = self.font.render(name, False, TEXT_COLOR)
        title_rect = title_surface.get_rect(midtop=self.rect.midtop + pygame.math.Vector2(0, 20))

        # Cost text
        cost_surface = self.font.render(f'{int(cost)}', False, TEXT_COLOR)
        cost_rect = cost_surface.get_rect(midbottom=self.rect.midbottom - pygame.math.Vector2(0, 20))

        # Draw
        surface.blit(title_surface, title_rect)
        surface.blit(cost_surface, cost_rect)

    def display(self, surface, selection_num, name, value, max_value, cost):
        pygame.draw.rect(surface, UI_BG_COLOR, self.rect)

        self.display_names(surface, name, cost, False)
