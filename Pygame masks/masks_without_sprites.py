import pygame
import sys


def quit_game():
    pygame.quit()
    sys.exit()


pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

# Player
player_surface = pygame.Surface((50, 50))
player_surface.fill('Red')
player_rect = player_surface.get_rect(center=(300, 300))
player_mask = pygame.mask.from_surface(player_surface)

# Obstacle
obstacle_surface = pygame.image.load('alpha.png').convert_alpha()
obstacle_position = (100, 100)
obstacle_mask = pygame.mask.from_surface(obstacle_surface)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()

    # Movement
    if pygame.mouse.get_pos():
        player_rect.center = pygame.mouse.get_pos()

    # Collisions
    offset_x = obstacle_position[0] - player_rect.left
    offset_y = obstacle_position[1] - player_rect.top
    # collision with one single point of overlap
    collision_point = player_mask.overlap(obstacle_mask, (offset_x, offset_y))
    if collision_point:
        print(f"Collision point: {collision_point}")
    # collision with an area of overlap
    collision_area = player_mask.overlap_area(obstacle_mask, (offset_x, offset_y))
    if collision_area:
        print(f"Area of collision: {collision_area}")
    # collision with a given area size
    if player_mask.overlap_area(obstacle_mask, (offset_x, offset_y)) >= 10:
        print(f"Collision with area of {collision_area}. That area is >= 10")

    # Draw
    screen.fill('White')
    screen.blit(obstacle_surface, obstacle_position)
    screen.blit(player_surface, player_rect)

    # Update screen
    pygame.display.update()
    clock.tick(60)
