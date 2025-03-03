import pygame
import sys
from settings import *
from functions import *

# Initialize
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(CAPTION)
clock = pygame.time.Clock()
text_font = pygame.font.Font('../font/Pixeltype.ttf', 70)

# Create surfaces
sky_surface = pygame.image.load("../graphics/Sky.png").convert()
ground_surface = pygame.image.load("../graphics/ground.png").convert()
text_surface = text_font.render('My game', True, 'Black')

snail_surface = pygame.image.load('../graphics/snail/snail1.png').convert_alpha()
snail_rectangle = snail_surface.get_rect(topleft=SNAIL_POSITION)

player_surface = pygame.image.load('../graphics/Player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(topleft=(80, 215))

# Main loop
while True:

    # Check for quit input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()

    # Position the surfaces on the display surface
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))
    screen.blit(player_surface, player_rectangle)
    screen.blit(snail_surface, snail_rectangle)

    # Move snail
    snail_rectangle.x -= SNAIL_SPEED
    # Check for out of bounds
    if snail_rectangle.right <= 0:
        snail_rectangle.left = 800

    # Check for collision
    if player_rectangle.colliderect(snail_rectangle):
        quit_game()

    # Update everything
    pygame.display.update()
    clock.tick(FRAME_RATE)


