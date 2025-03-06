import pygame
import sys


# Functions
def move_ball():
    ball.x += ball_speed_x
    ball.y += ball_speed_y


def move_player():
    player.y += player_speed


def move_opponent():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed


def check_collisions():
    global ball_speed_y, ball_speed_x, player_score, opponent_score
    # Check ball border collisions
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    # Check players out of bounds
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height
    # opponent scores
    if ball.left <= 0:
        ball.left = 1
        ball_speed_x *= -1
        opponent_score += 1
    # player scores
    if ball.right > screen_width:
        ball.right = screen_width - 1
        ball_speed_x *= -1
        player_score += 1
    # Check player-ball collisions
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1


def check_score():
    global winner, game_active
    if player_score == winning_score:
        game_active = False
        winner = 'player'
    if opponent_score == winning_score:
        game_active = False
        winner = 'opponent'


def display_score():
    score_surface = font.render(f"Player: {player_score}    Opponent: {opponent_score}", True, 'White').convert_alpha()
    score_rect = score_surface.get_rect(center=(screen_width / 2 + 30, 40))
    screen.blit(score_surface, score_rect)


def display_winner():
    win_surface = font.render(f"{winner} won!", True, 'Black').convert_alpha()
    win_rect = win_surface.get_rect(center=(screen_width / 2, 50))
    screen.blit(win_surface, win_rect)


def display_endgame_options():
    # Replay message
    replay_surface = font.render("Press Enter to replay.", True, 'Black').convert_alpha()
    replay_rect = replay_surface.get_rect(center=(screen_width / 2, 230))
    screen.blit(replay_surface, replay_rect)
    # Quit message
    quit_surface = font.render("Press 'q' to quit.", True, 'Black').convert_alpha()
    quit_rect = quit_surface.get_rect(center=(screen_width / 2, 430))
    screen.blit(quit_surface, quit_rect)


def exit_game():
    pygame.quit()
    sys.exit()


# General setup
pygame.init()
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)

# Setting up the main window
screen_width = 1280
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# Game rectangles
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player = pygame.Rect(10, screen_height / 2 - 70, 10, 140)
opponent = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)

# Colors
background_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

# Speed
ball_speed_x = 7
ball_speed_y = 7
player_speed = 0
opponent_speed = 5

# Gameplay
winner = ''
player_score = 0
opponent_score = 0
winning_score = 2

game_active = True

while True:
    if game_active:
        # Handle input
        for event in pygame.event.get():
            # quit
            if event.type == pygame.QUIT:
                exit_game()
            # player movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    player_speed += 7
                if event.key == pygame.K_UP:
                    player_speed -= 7
            # player stop
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    player_speed -= 7
                if event.key == pygame.K_UP:
                    player_speed += 7

        # Ball
        move_ball()
        check_collisions()

        # Players
        move_player()
        move_opponent()

        # Draw elements
        screen.fill(background_color)
        pygame.draw.rect(screen, light_grey, player)
        pygame.draw.rect(screen, light_grey, opponent)
        pygame.draw.ellipse(screen, light_grey, ball)
        # draw the middle line
        pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height))

        # Score
        check_score()
        display_score()
    else:
        # Handle input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()
            if event.type == pygame.KEYDOWN:
                # Restart game
                if event.key == pygame.K_RETURN:
                    game_active = True
                    # reset stats
                    winner = ''
                    player_score = 0
                    opponent_score = 0
                    ball.x = screen_width / 2 - 15
                    ball.y = screen_height / 2 - 15
                    ball_speed_x = 7
                    ball_speed_y = 7
                    player.y = screen_height / 2 - 70
                    opponent.y = screen_height / 2 - 70
                if event.key == pygame.K_q:
                    exit_game()

        # Endgame screen
        screen.fill('Yellow')
        display_winner()
        display_endgame_options()

    # Update the window
    pygame.display.flip()
    clock.tick(60)


