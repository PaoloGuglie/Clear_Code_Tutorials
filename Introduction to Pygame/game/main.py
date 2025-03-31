#                   IMPORTS
import random

import pygame
import sys
from random import choice
from settings import *

#               GLOBAL
SCORE = 0
START_TIME = 0
FINAL_TIME = 0


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

        # Jump sound
        self.jump_sound = pygame.mixer.Sound('../audio/jump.mp3')
        self.jump_sound.set_volume(0.2)

    def player_input(self):
        keys = pygame.key.get_pressed()
        # Jump
        if keys[pygame.K_SPACE] and self.rect.y >= 215:
            self.gravity = -20
            self.jump_sound.play()

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


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        # Get the correct obstacle
        if type == 'fly':
            fly_1 = pygame.image.load('../graphics/Fly/Fly1.png').convert_alpha()
            fly_2 = pygame.image.load('../graphics/Fly/Fly2.png').convert_alpha()
            self.frames = [fly_1, fly_2]
            y_pos = 190
        else:
            snail_1 = pygame.image.load('../graphics/snail/snail1.png').convert_alpha()
            snail_2 = pygame.image.load('../graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 300
        # Create the image and rectangle
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(random.randint(900, 1000), y_pos))

    def animation(self):
        self.animation_index += 0.1
        self.image = self.frames[int(self.animation_index) % 2]

    def destroy(self):
        global SCORE
        if self.rect.x <= -50:
            self.kill()  # built-in method
            SCORE += 1   # increase score

    def update(self):
        self.animation()
        self.rect.x -= 6  # move sprite
        self.destroy()


#                   FUNCTIONS
def quit_game():
    pygame.quit()
    sys.exit()


def display_score():
    score_surface = text_font.render(f'Score: {SCORE}', True, 'Black')
    score_rect = score_surface.get_rect(center=(350, 50))
    screen.blit(score_surface, score_rect)


def display_time():
    current_time = int(pygame.time.get_ticks() / 1000) - START_TIME
    time_surface = text_font.render(f'Time: {current_time}', True, 'Black')
    time_rect = time_surface.get_rect(center=(600, 50))
    screen.blit(time_surface, time_rect)


def display_final_time():
    time_surface = text_font.render(f'Time: {FINAL_TIME}', True, 'Black')
    time_rect = time_surface.get_rect(center=(600, 50))
    screen.blit(time_surface, time_rect)


def collision():
    global FINAL_TIME
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):  # returns a collision list
        obstacle_group.empty()
        FINAL_TIME = int(pygame.time.get_ticks() / 1000) - START_TIME
        return False
    else:
        return True


#                   INITIALIZE
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(CAPTION)
clock = pygame.time.Clock()
text_font = pygame.font.Font('../font/Pixeltype.ttf', 70)
background_music = pygame.mixer.Sound('../audio/music.wav')
background_music.set_volume(0.1)

# Create environment surfaces
sky_surface = pygame.image.load("../graphics/Sky.png").convert()
ground_surface = pygame.image.load("../graphics/ground.png").convert()

# Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

# Obstacle spawn timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, SPAWN_TIME)

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
                    # Start music
                    background_music.play()
                    background_music.play(loops=-1)
                elif event.key == pygame.K_q:
                    quit_game()

        if GAME_ACTIVE:
            # TIMER EVENTS
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['snail', 'snail', 'fly'])))

    if GAME_ACTIVE:
        # Position the items on the display surface
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))

        # Player
        player.draw(screen)
        player.update()

        # Obstacles
        obstacle_group.draw(screen)
        obstacle_group.update()

        # Display score and time
        display_score()
        display_time()

        # Check for collisions
        GAME_ACTIVE = collision()

    else:
        # Stop music
        background_music.stop()

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


