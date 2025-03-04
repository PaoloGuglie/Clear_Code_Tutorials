# Import statements
import pygame
from settings import *
from functions import *

# Initialize
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(CAPTION)
clock = pygame.time.Clock()
text_font = pygame.font.Font('../font/Pixeltype.ttf', 70)

# Create environment surfaces
sky_surface = pygame.image.load("../graphics/Sky.png").convert()
ground_surface = pygame.image.load("../graphics/ground.png").convert()

# Create score surface and rectangle
score_surface = text_font.render(f'Score: {SCORE}', True, (64, 64, 64))
score_rect = score_surface.get_rect(center=(400, 50))

# Create snail surface and rectangle
snail_surface = pygame.image.load('../graphics/snail/snail1.png').convert_alpha()
snail_rectangle = snail_surface.get_rect(topleft=SNAIL_POSITION)

# Create player surface and rectangle
player_surface = pygame.image.load('../graphics/Player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(topleft=(80, 215))

# Main loop
while True:

    # Check for inputs
    for event in pygame.event.get():
        # Quit
        if event.type == pygame.QUIT:
            quit_game()
        # Mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
        # Jump
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if player_rectangle.y == 215:
                    PLAYER_GRAVITY = -20

    # Position the items on the display surface
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))

    pygame.draw.rect(screen, '#c0e8ec', score_rect)
    screen.blit(score_surface, score_rect)

    screen.blit(player_surface, player_rectangle)
    screen.blit(snail_surface, snail_rectangle)

    # Move the player
    if PLAYER_GRAVITY < 0 or player_rectangle.y != 215:
        PLAYER_GRAVITY += 1
        player_rectangle.y += PLAYER_GRAVITY

    # Move the snail
    snail_rectangle.x -= SNAIL_SPEED
    # Check if the snail reached end of screen
    if snail_rectangle.right <= 0:
        # Move snail back to start
        snail_rectangle.left = 800
        # Update score
        SCORE += 1
        score_surface = text_font.render(f'Score: {SCORE}', True, (64, 64, 64))

    # Check for collision
    if player_rectangle.colliderect(snail_rectangle):
        print(f"Snail collision! Score: {SCORE}")
        quit_game()

    # Check for mouse collision with the player
    mouse_position = pygame.mouse.get_pos()
    if player_rectangle.collidepoint(mouse_position):
        print("Mouse collision!")

    # Update everything
    pygame.display.update()
    clock.tick(FRAME_RATE)


