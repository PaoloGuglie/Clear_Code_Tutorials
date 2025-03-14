import pygame
import sys


def quit_game():
    pygame.quit()
    sys.exit()


pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

# Obstacle
obstacle_surface = pygame.image.load('alpha.png').convert_alpha()
obstacle_position = (100, 100)
# create obstacle mask
obstacle_mask = pygame.mask.from_surface(obstacle_surface)
# turn mask back into surface
new_obstacle_surface = obstacle_mask.to_surface()
# remove black from new surface
new_obstacle_surface.set_colorkey((0, 0, 0))  # tuple specifies which color has to disappear (in this case, black)
# change every white pixel's color to fill in the surface
surface_width, surface_height = new_obstacle_surface.get_size()
for x in range(surface_width):
    for y in range(surface_height):
        if new_obstacle_surface.get_at((x, y))[0] != 0:
            new_obstacle_surface.set_at((x, y), 'orange')  # now the alpha letter is orange

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()

    # Draw
    screen.fill('grey')
    screen.blit(obstacle_surface, obstacle_position)
    screen.blit(new_obstacle_surface, obstacle_position)

    # Refresh screen
    pygame.display.update()
    clock.tick(60)
