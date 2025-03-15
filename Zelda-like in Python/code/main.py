import pygame
import sys

from settings import *


def quit_game():
    pygame.quit()
    sys.exit()


class Game:
    def __init__(self):

        # Setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            # Check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_game()

            # Draw elements
            self.screen.fill('Black')

            # Refresh game
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
