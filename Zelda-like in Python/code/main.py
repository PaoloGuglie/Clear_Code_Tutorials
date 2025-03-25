import pygame
import sys

from settings import *
from level import Level


def quit_game():
    pygame.quit()
    sys.exit()


class Game:
    def __init__(self):
        # Setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Zelda")
        self.clock = pygame.time.Clock()

        self.level = Level()

    def run(self):
        while True:
            # Check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_game()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:  # menu button
                        self.level.toggle_menu()

            # Background
            self.screen.fill(WATER_COLOR)

            # Run the level
            self.level.run()

            # Refresh the game
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
