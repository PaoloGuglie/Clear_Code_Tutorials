import pygame

from settings import *


class UI:
    def __init__(self):

        # General info
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        # Bar setup
        self.health_bar_rect = pygame.Rect(10, 10, HEALTH_BAR_WIDTH, BAR_HEIGHT)
        self.energy_bar_rect = pygame.Rect(10, 34, ENERGY_BAR_WIDTH, BAR_HEIGHT)

        # Convert weapon dictionary
        self.weapon_graphics = [pygame.image.load(i['graphic']).convert_alpha() for i in weapon_data.values()]

    def show_bar(self, current_amount, max_amount, bg_rect, color):

        # Draw background
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)

        # Convert stat to pixel
        ratio = current_amount / max_amount
        current_width = bg_rect.width * ratio

        # Get current amount rect
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        # Draw bar
        pygame.draw.rect(self.display_surface, color, current_rect)
        # bar border
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 5)

    def show_exp(self, exp):
        # rect
        text_surface = self.font.render(str(int(exp)), False, TEXT_COLOR)
        x_pos = self.display_surface.get_width() - 20
        y_pos = self.display_surface.get_height() - 20
        text_rect = text_surface.get_rect(bottomright=(x_pos, y_pos))
        # background
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, text_rect.inflate(20, 10))
        # background frame
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, text_rect.inflate(20, 10), 5)
        # text
        self.display_surface.blit(text_surface, text_rect)

    def selection_box(self, left, top, has_switched):
        bg_rect = pygame.Rect(left, top, ITEM_BOX_SIZE, ITEM_BOX_SIZE)
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)
        # box bordes styles
        if has_switched:
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOR_ACTIVE, bg_rect, 5)

        else:
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 5)

        return bg_rect

    def weapon_overlay(self, weapon_index, has_switched):
        bg_rect = self.selection_box(10, 620, has_switched)

        # Weapon
        weapon_surface = self.weapon_graphics[weapon_index]
        weapon_rect = weapon_surface.get_rect(center=bg_rect.center)

        self.display_surface.blit(weapon_surface, weapon_rect)

    def magic_overlay(self, has_switched):
        bg_rect = self.selection_box(75, 628, has_switched)

        # Magic

    def display(self, player):
        # health bar
        self.show_bar(
            player.health,
            player.stats['health'],
            self.health_bar_rect,
            HEALTH_COLOR
        )
        # energy bar
        self.show_bar(
            player.energy,
            player.stats['energy'],
            self.energy_bar_rect,
            ENERGY_COLOR
        )
        # exp count
        self.show_exp(player.exp)
        # selection boxes
        self.magic_overlay(not player.can_switch_magic)
        self.weapon_overlay(player.weapon_index, not player.can_switch_weapon)
