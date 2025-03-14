import pygame
import sys


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill('red')
        self.rect = self.image.get_rect(center=(300, 300))
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        """ The center of the rectangle follows the mouse """
        if pygame.mouse.get_pos():
            self.rect.center = pygame.mouse.get_pos()


class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('alpha.png').convert_alpha()
        self.rect = self.image.get_rect(center=(400, 400))
        self.mask = pygame.mask.from_surface(self.image)


def quit_game():
    pygame.quit()
    sys.exit()


pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

# Group setup
player = pygame.sprite.GroupSingle(Player())
obstacle = pygame.sprite.GroupSingle(Obstacle())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()

    # Update
    player.update()

    # First, check if there is a rectangle collision, then check if there is a
    # mask collision. This improves performance instead of checking every time
    # for a mask collision (every pixel for both sprites).
    # This will check for a mask collision if both sprites are very close to
    # each other. The code will run a lot faster.
    if pygame.sprite.spritecollide(player.sprite, obstacle, False):
        if pygame.sprite.spritecollide(player.sprite, obstacle, False, pygame.sprite.collide_mask):
            player.sprite.image.fill('green')
        else:
            player.sprite.image.fill('red')

    # Draw
    screen.fill('White')
    obstacle.draw(screen)
    player.draw(screen)

    # Display update
    pygame.display.update()
    clock.tick(60)
