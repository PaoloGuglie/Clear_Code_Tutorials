import pygame
import sys


def quit_game():
    pygame.quit()
    sys.exit()


def create_simple_outline():
    screen.blit(obstacle_surface, obstacle_position)
    screen.blit(new_obstacle_surface, obstacle_position)

    for point in obstacle_mask.outline():
        x = point[0] + obstacle_position[0]
        y = point[1] + obstacle_position[1]
        pygame.draw.circle(screen, 'black', (x, y), 4)


def create_complex_outline():
    offset = 10
    screen.blit(new_obstacle_surface, (obstacle_position[0] + offset, obstacle_position[1]))  # right
    screen.blit(new_obstacle_surface, (obstacle_position[0] - offset, obstacle_position[1]))  # left
    screen.blit(new_obstacle_surface, (obstacle_position[0], obstacle_position[1] - offset))  # top
    screen.blit(new_obstacle_surface, (obstacle_position[0], obstacle_position[1] + offset))  # bottom
    screen.blit(new_obstacle_surface, (obstacle_position[0] + offset, obstacle_position[1] - offset))  # top-right
    screen.blit(new_obstacle_surface, (obstacle_position[0] + offset, obstacle_position[1] + offset))  # bottom-right
    screen.blit(new_obstacle_surface, (obstacle_position[0] - offset, obstacle_position[1] + offset))  # bottom-left
    screen.blit(new_obstacle_surface, (obstacle_position[0] - offset, obstacle_position[1] - offset))  # topleft

    screen.blit(obstacle_surface, obstacle_position)


# Choose outline
choice = input("Choose the outline: simple (s) or complex (c):  - ")

# Initialize pygame
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

    if choice == "s":
        create_simple_outline()

    elif choice == "c":
        create_complex_outline()

    else:
        print("Wrong input. Rerun the program and type better!")
        quit_game()

    # Refresh screen
    pygame.display.update()
    clock.tick(60)
