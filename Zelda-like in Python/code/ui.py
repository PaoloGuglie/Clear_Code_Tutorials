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
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)

    def show_exp(self, exp):
        # rect
        text_surface = self.font.render(str(int(exp)), False, TEXT_COLOR)
        x_pos = self.display_surface.get_width() - 20
        y_pos = self.display_surface.get_height() - 20
        text_rect = text_surface.get_rect(bottomright=(x_pos, y_pos))
        # background
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, text_rect.inflate(20, 10))
        # background frame
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, text_rect.inflate(20, 10), 3)
        # text
        self.display_surface.blit(text_surface, text_rect)

    def display(self, player):
        self.show_bar(
            player.health,
            player.stats['health'],
            self.health_bar_rect,
            HEALTH_COLOR
        )
        self.show_bar(
            player.energy,
            player.stats['energy'],
            self.energy_bar_rect,
            ENERGY_COLOR
        )
        self.show_exp(player.exp)
