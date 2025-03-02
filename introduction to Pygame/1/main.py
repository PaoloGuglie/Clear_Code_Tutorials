import pygame
import sys
from settings import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(CAPTION)
clock = pygame.time.Clock()

# Create surfaces
sky_surface = pygame.image.load("../graphics/Sky.png")
ground_surface = pygame.image.load("../graphics/ground.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Position the surfaces on the display surface
    screen.blit(sky_surface, (200, 100))
    screen.blit(ground_surface, (500, 300))

    # Draw all my elements
    # Update everything
    pygame.display.update()
    clock.tick(FRAME_RATE)


