import pygame
import sys


def quit_game():
    pygame.quit()
    sys.exit()


# Initialize
pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

# Ship
ship_surface = pygame.image.load('ship.png').convert_alpha()
ship_rect = ship_surface.get_rect(center=(300, 300))
ship_mask = pygame.mask.from_surface(ship_surface)

# Obstacle
obstacle_surface = pygame.image.load('alpha.png').convert_alpha()
obstacle_pos = (100, 100)
obstacle_mask = pygame.mask.from_surface(obstacle_surface)

# Main loop
while True:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()

    # Move
    if pygame.mouse.get_pos():
        ship_rect.center = pygame.mouse.get_pos()

    # Draw
    screen.fill('White')
    screen.blit(obstacle_surface, obstacle_pos)
    screen.blit(ship_surface, ship_rect)

    # New mask surface coloring
    offset_x = obstacle_pos[0] - ship_rect.left
    offset_y = obstacle_pos[1] - ship_rect.top
    if ship_mask.overlap(obstacle_mask, (offset_x, offset_y)):
        new_mask = ship_mask.overlap_mask(obstacle_mask, (offset_x, offset_y))
        new_surface = new_mask.to_surface()
        new_surface.set_colorkey((0, 0, 0))  # to not display the color black

        # Color the overlapping pixels
        surface_width, surface_height = new_surface.get_size()
        for x in range(surface_width):
            for y in range(surface_height):
                if new_surface.get_at((x, y))[0] != 0:  # check if it is not black
                    new_surface.set_at((x, y), 'red')

        screen.blit(new_surface, ship_rect)

    # Update screen
    pygame.display.update()
    clock.tick(60)
