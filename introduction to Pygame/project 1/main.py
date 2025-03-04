# Import statements
import pygame
import sys
from settings import *


# Functions
def quit_game():
    pygame.quit()
    sys.exit()


def display_score():
    score_surface = text_font.render(f'Score: {SCORE}', True, 'Black')
    score_rect = score_surface.get_rect(center=(350, 50))
    screen.blit(score_surface, score_rect)


def display_time():
    current_time = int(pygame.time.get_ticks() / 1000 - START_TIME)
    time_surface = text_font.render(f'Time: {current_time}', True, 'Black')
    time_rect = time_surface.get_rect(center=(600, 50))
    screen.blit(time_surface, time_rect)


def display_final_time():
    time_surface = text_font.render(f'Time: {FINAL_TIME - START_TIME}', True, 'Black')
    time_rect = time_surface.get_rect(center=(600, 50))
    screen.blit(time_surface, time_rect)


# Initialize
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(CAPTION)
clock = pygame.time.Clock()
text_font = pygame.font.Font('../font/Pixeltype.ttf', 70)

# Create environment surfaces
sky_surface = pygame.image.load("../graphics/Sky.png").convert()
ground_surface = pygame.image.load("../graphics/ground.png").convert()

# Create snail surface and rectangle
snail_surface = pygame.image.load('../graphics/snail/snail1.png').convert_alpha()
snail_rectangle = snail_surface.get_rect(topleft=SNAIL_POSITION)

# Create player surface and rectangle
player_surface = pygame.image.load('../graphics/Player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(topleft=(80, 215))

# Main loop
while True:

    # INPUTS
    for event in pygame.event.get():
        # Quit
        if event.type == pygame.QUIT:
            quit_game()

        if GAME_ACTIVE:
            # Jump
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player_rectangle.y == 215:
                        PLAYER_GRAVITY = -20

        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Restart the game
                    GAME_ACTIVE = True
                    # Reposition the snail
                    snail_rectangle.left = 800
                    # Reset score and time
                    SCORE = 0
                    START_TIME = int(pygame.time.get_ticks() / 1000)
                elif event.key == pygame.K_q:
                    quit_game()

    if GAME_ACTIVE:
        # Position the items on the display surface
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))

        screen.blit(player_surface, player_rectangle)
        screen.blit(snail_surface, snail_rectangle)

        # Display score and time
        display_score()
        display_time()

        # Jump behaviour
        if PLAYER_GRAVITY < 0 or player_rectangle.y != 215:
            PLAYER_GRAVITY += 1
            player_rectangle.y += PLAYER_GRAVITY

        # Move the snail
        snail_rectangle.x -= SNAIL_SPEED
        # Check if the snail reached end of screen
        if snail_rectangle.right <= 0:
            # Move snail back to start
            snail_rectangle.left = 800
            # Update score and text
            SCORE += 1
            display_score()

        # Check for player-snail collision
        if player_rectangle.colliderect(snail_rectangle):
            # Game over
            GAME_ACTIVE = False
            # Get current time
            FINAL_TIME = int(pygame.time.get_ticks() / 1000)

    else:
        # Game over screen
        screen.fill('Yellow')

        # Display elements
        display_score()
        display_final_time()

        # Replay message
        replay_msg_surface = text_font.render("Press Enter to replay", True, 'Black')
        replay_msg_rect = replay_msg_surface.get_rect(center=(400, 200))
        screen.blit(replay_msg_surface, replay_msg_rect)

        # Quit message
        quit_msg_surface = text_font.render("Press 'q' to quit", True, 'Black')
        quit_msg_rect = quit_msg_surface.get_rect(center=(400, 300))
        screen.blit(quit_msg_surface, quit_msg_rect)

    # Update everything
    pygame.display.update()
    clock.tick(FRAME_RATE)


