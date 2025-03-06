#                   IMPORTS
import pygame
import sys
from random import randint
from settings import *


#                   CLASSES
class Player(pygame.sprite.Sprite):
    def __init__(self):
        # Data
        super().__init__()
        player_walk_1 = pygame.image.load('../graphics/Player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('../graphics/Player/player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_jump = pygame.image.load('../graphics/Player/jump.png').convert_alpha()
        self.player_index = 0
        # Default sprite
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(topleft=(50, 215))
        self.gravity = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        # Jump
        if keys[pygame.K_SPACE] and self.rect.y >= 215:
            self.gravity = -20

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.y >= 215:
            self.rect.y = 215

    def animation(self):
        if self.rect.bottom < 215:
            # Show jump animation
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            self.image = self.player_walk[int(self.player_index) % 2]  # Clever by me!

    # Run the other functions
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation()


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
            obstacle_rect.x -= OBSTACLE_SPEED

            # Snail or Fly?
            if obstacle_rect.bottom == 300:
                screen.blit(snail_surface, obstacle_rect)
            else:
                screen.blit(fly_surface, obstacle_rect)

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

# Snail assets
snail_frame_1 = pygame.image.load('../graphics/snail/snail1.png').convert_alpha()
snail_frame_2 = pygame.image.load('../graphics/snail/snail2.png').convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_frame_index = 0
snail_surface = snail_frames[snail_frame_index]

# Fly assets
fly_frame_1 = pygame.image.load('../graphics/Fly/Fly1.png').convert_alpha()
fly_frame_2 = pygame.image.load('../graphics/Fly/Fly2.png').convert_alpha()
fly_frames = [fly_frame_1, fly_frame_2]
fly_frame_index = 0
fly_surface = fly_frames[fly_frame_index]

# Obstacles list
obstacle_rect_list = []

# Player
player = pygame.sprite.GroupSingle()
player.add(Player())

# Obstacle spawn timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, SPAWN_TIME)

# Snail animation timer
snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

# Fly animation timer
fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

#                   MAIN LOOP
while True:

    # CHECK INPUTS
    for event in pygame.event.get():
        # Quit
        if event.type == pygame.QUIT:
            quit_game()

        if not GAME_ACTIVE:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Restart the game
                    GAME_ACTIVE = True

                    # Reset score and time
                    SCORE = 0
                    START_TIME = int(pygame.time.get_ticks() / 1000)
                elif event.key == pygame.K_q:
                    quit_game()

        if GAME_ACTIVE:
            # TIMER EVENTS
            if event.type == obstacle_timer:
                if randint(0, 2):
                    obstacle_rect_list.append(snail_frame_1.get_rect(bottomright=(randint(900, 1000), 300)))
                else:
                    obstacle_rect_list.append(fly_frame_1.get_rect(bottomright=(randint(900, 1000), 190)))

            if event.type == snail_animation_timer:
                snail_frame_index = 1 if snail_frame_index == 0 else 0
                snail_surface = snail_frames[snail_frame_index]

            if event.type == fly_animation_timer:
                fly_frame_index = 1 if fly_frame_index == 0 else 0
                fly_surface = fly_frames[fly_frame_index]

    if GAME_ACTIVE:
        # Position the items on the display surface
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))

        # Player
        player.draw(screen)
        player.update()

        # Display score and time
        display_score()
        display_time()

        # Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # Check if the obstacle reached end of screen
        for obstacle in obstacle_rect_list:
            if -3 <= obstacle.x <= 4:
                # Update score and text
                SCORE += 1
                display_score()

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


