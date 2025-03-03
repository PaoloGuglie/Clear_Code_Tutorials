import pygame
import sys
from settings import *

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

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Position the surfaces on the display surface
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))
    screen.blit(snail_surface, (SNAIL_X_POS, 265))

    # Move snail
    SNAIL_X_POS -= 4

    # Check for EOS (End Of Screen)
    if SNAIL_X_POS <= -100:
        SNAIL_X_POS = 810

    # Update everything
    pygame.display.update()
    clock.tick(FRAME_RATE)


