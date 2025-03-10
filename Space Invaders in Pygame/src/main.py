import pygame
import sys
import json

from settings import settings, update_settings
from player import Player
from alien import Alien
import obstacle


class Game:
    """All the game logic will go inside this class"""

    def __init__(self):
        # Player
        player_sprite = Player((settings["screen"]["width"] / 2, settings["screen"]["height"]))
        self.player = pygame.sprite.GroupSingle(player_sprite)

        # Obstacle
        self.shape = obstacle.shape
        self.block_size = settings["obstacle"]["block-size"]
        self.blocks = pygame.sprite.Group()
        self.obstacle_amount = settings["obstacle"]["quantity"]
        self.obstacle_x_positions = [num * (settings["screen"]["width"] / self.obstacle_amount) for num in range(self.obstacle_amount)]
        self.create_multiple_obstacles(45, 480, self.obstacle_x_positions)

        # Alien
        self.aliens = pygame.sprite.Group()
        self.alien_setup(6, 8, 60, 48, 70, 40)

    def create_obstacle(self, x_start, y_start, offset_x):
        """ Block positioning logic per obstacle """
        for row_index, row in enumerate(self.shape):
            for col_index, col in enumerate(row):
                if col == 'x':
                    # include start position and offset
                    x = x_start + col_index * self.block_size + offset_x
                    y = y_start + row_index * self.block_size
                    block = obstacle.Block(self.block_size, 'Red', x, y)
                    self.blocks.add(block)

    def create_multiple_obstacles(self, x_start, y_start, offset_list):
        """ Number of obstacles positioned and distance between them """
        for x in offset_list:
            self.create_obstacle(x_start, y_start, x)

    def alien_setup(self, rows, cols, x_distance, y_distance, x_offset, y_offset):
        """ Position aliens on multiple rows """
        for row_index, row in enumerate(range(rows)):
            for col_index, col in enumerate(range(cols)):
                x_pos = col_index * x_distance + x_offset
                y_pos = row_index * y_distance + y_offset

                if row_index == 0:
                    alien_sprite = Alien("yellow", x_pos, y_pos)
                elif 1 <= row_index <= 2:
                    alien_sprite = Alien("green", x_pos, y_pos)
                else:
                    alien_sprite = Alien("red", x_pos, y_pos)
                self.aliens.add(alien_sprite)

    def alien_position_checker(self):
        for alien in self.aliens.sprites():
            if alien.rect.right >= settings["screen"]["width"] or alien.rect.left <= 0:
                # change direction
                settings["alien"]["movement"]["x_direction"] *= -1
                update_settings(settings)
                # move down
                self.alien_move_down(settings["alien"]["movement"]["y_drop"])
                break

    def alien_move_down(self, distance):
        if self.aliens:
            for alien in self.aliens.sprites():
                alien.rect.y += distance

    def run(self):
        # Update sprite groups
        self.player.update()  # (update player and lasers)
        self.aliens.update(settings["alien"]["movement"]["x_direction"])
        self.alien_position_checker()
        # Draw sprite groups
        self.player.draw(screen)
        self.aliens.draw(screen)
        self.player.sprite.lasers.draw(screen)
        self.blocks.draw(screen)


def quit_game():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    # Initialize
    pygame.init()
    screen = pygame.display.set_mode((settings["screen"]["width"], settings["screen"]["height"]))
    clock = pygame.time.Clock()
    game = Game()

    while True:
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        # Update and draw elements
        screen.fill('Black')
        game.run()

        # Refresh
        pygame.display.flip()
        clock.tick(60)
