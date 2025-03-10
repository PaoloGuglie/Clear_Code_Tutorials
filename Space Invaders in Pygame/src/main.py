import pygame
import sys
import json

from settings import settings, update_settings
from player import Player


class Game:
    """All the game logic will go inside this class"""

    def __init__(self):
        # Add sprite groups
        player_sprite = Player((settings["screen"]["width"] / 2, settings["screen"]["height"]))
        self.player = pygame.sprite.GroupSingle(player_sprite)

    def run(self):
        # Update sprite groups

        # Draw sprite groups
        self.player.draw(screen)


def quit_game():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    # Initialize
    pygame.init()
    screen = pygame.display.set_mode((settings["screen"]["width"], settings["screen"]["height"]))
    clock = pygame.time.Clock()
    game = Game()

    settings["player"]["speed"] = 5
    update_settings()

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
