import pygame
import sys
import json


def render_red_score():
    red_score_surface = game_font.render(f'Clicks: {score['red']}', True, 'White')
    red_score_rect = red_score_surface.get_rect(center=(250, 350))
    screen.blit(red_score_surface, red_score_rect)


def render_blue_score():
    blue_score_surface = game_font.render(f'Clicks: {score['blue']}', True, 'White')
    blue_score_rect = blue_score_surface.get_rect(center=(550, 350))
    screen.blit(blue_score_surface, blue_score_rect)


def get_starting_score():
    global score
    try:
        with open('score.txt', 'r') as score_file:
            score = json.load(score_file)
    except FileNotFoundError:
        score = {
            'red': 0,
            'blue': 0
        }


def reset_score():
    with open('score.txt', 'w') as score_file:
        reset_score = {
            'red': 0,
            'blue': 0
        }
        json.dump(reset_score, score_file)

    get_starting_score()


def quit_game():
    # draw to json
    with open('score.txt', 'w') as score_file:
        json.dump(score, score_file)
    # close game
    pygame.quit()
    sys.exit()


# Initialize game
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
game_font = pygame.font.Font(None, 32)
# get stored score or create one
get_starting_score()


# Rectangles
red_surface = pygame.Surface([200, 200])
red_surface.fill('Red')
red_rect = red_surface.get_rect(center=(250, 200))

blue_surface = pygame.Surface([200, 200])
blue_surface.fill('Blue')
blue_rect = blue_surface.get_rect(center=(550, 200))

# create button surface
reset_button_surface = pygame.Surface([200, 100])
reset_button_surface.fill('Pink')
# create text surface and rect
reset_text_surface = game_font.render("RESET", True, 'Black')
reset_text_rect = reset_text_surface.get_rect(center=(reset_button_surface.get_width() // 2,
                                              reset_button_surface.get_height() // 2))
# add the text surface and rect to the button surface
reset_button_surface.blit(reset_text_surface, reset_text_rect)
# get the button rect
reset_button_rect = reset_button_surface.get_rect(center=(400, 480))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if red_rect.collidepoint(event.pos):
                score['red'] += 1
            if blue_rect.collidepoint(event.pos):
                score['blue'] += 1
            if reset_button_rect.collidepoint(event.pos):
                reset_score()

    # Draw elements
    screen.fill('Black')

    screen.blit(red_surface, red_rect)
    screen.blit(blue_surface, blue_rect)
    screen.blit(reset_button_surface, reset_button_rect)

    render_red_score()
    render_blue_score()

    # Refresh game
    pygame.display.update()
    clock.tick(60)

