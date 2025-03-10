import pygame
import sys
import json

from settings import settings, update_settings
from player import Player
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
        self.create_obstacle(40, 480)

    def create_obstacle(self, x_start, y_start):
        for row_index, row in enumerate(self.shape):
            for col_index, col in enumerate(row):
                if col == 'x':
                    x = x_start + col_index * self.block_size
                    y = y_start + row_index * self.block_size
                    block = obstacle.Block(self.block_size, 'Red', x, y)
                    self.blocks.add(block)

    def run(self):
        # Update sprite groups
        self.player.update()  # (update player and lasers)
        # Draw sprite groups
        self.player.draw(screen)
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
