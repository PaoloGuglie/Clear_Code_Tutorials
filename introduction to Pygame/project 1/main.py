#                   IMPORTS
import pygame
import sys
from random import randint
from settings import *


#                   FUNCTIONS
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


def obstacle_movement(obstacle_list):
    if obstacle_list:
        # Move the obstacles
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= SNAIL_SPEED
            screen.blit(snail_surface, obstacle_rect)

        # Delete out of bounds obstacles (using list comprehension)
        obstacle_list = [i for i in obstacle_list if i.x > -100]

        # Update list (target global scope)
        return obstacle_list
    else:
        return []


#                   INITIALIZE
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(CAPTION)
clock = pygame.time.Clock()
text_font = pygame.font.Font('../font/Pixeltype.ttf', 70)

# Create environment surfaces
sky_surface = pygame.image.load("../graphics/Sky.png").convert()
ground_surface = pygame.image.load("../graphics/ground.png").convert()

# Obstacles
snail_surface = pygame.image.load('../graphics/snail/snail1.png').convert_alpha()

obstacle_rect_list = []

# Create player surface and rectangle
player_surface = pygame.image.load('../graphics/Player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(topleft=(80, 215))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 2000)

#                   MAIN LOOP
while True:

    # CHECK INPUTS
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

                    # Reset score and time
                    SCORE = 0
                    START_TIME = int(pygame.time.get_ticks() / 1000)
                elif event.key == pygame.K_q:
                    quit_game()

        if event.type == obstacle_timer and GAME_ACTIVE:
            obstacle_rect_list.append(snail_surface.get_rect(bottomright=(randint(900, 1000), 300)))

    if GAME_ACTIVE:
        # Position the items on the display surface
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))

        screen.blit(player_surface, player_rectangle)

        # Display score and time
        display_score()
        display_time()

        # Player movement
        if PLAYER_GRAVITY < 0 or player_rectangle.y != 215:
            PLAYER_GRAVITY += 1
            player_rectangle.y += PLAYER_GRAVITY

        # Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # Check if the obstacle reached end of screen
        for obstacle in obstacle_rect_list:
            if -1 <= obstacle.x <= 4:
                # Update score and text
                SCORE += 1
                display_score()

        # Check for player-obstacle collision
        for obstacle in obstacle_rect_list:
            if player_rectangle.colliderect(obstacle):
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

        # Reset obstacles
        obstacle_rect_list = []

    # Update everything
    pygame.display.update()
    clock.tick(FRAME_RATE)


