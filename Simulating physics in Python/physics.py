import pygame
import sys
import pymunk


# Functions
def create_apple(space, pos):
    body = pymunk.Body(1, 100, body_type=pymunk.Body.DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body, 40)
    # add to physics simulation
    space.add(body, shape)
    return shape


def draw_apples(apples):
    for apple in apples:
        pos_x = int(apple.body.position.x)
        pos_y = int(apple.body.position.y)
        pygame.draw.circle(screen, 'Yellow', (pos_x, pos_y), 40)


def static_ball(space, pos):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = pos
    shape = pymunk.Circle(body, 35)
    space.add(body, shape)
    return shape


def draw_static_balls(balls):
    for ball in balls:
        ball_x = int(ball.body.position.x)
        ball_y = int(ball.body.position.y)
        pygame.draw.circle(screen, 'White', (ball_x, ball_y), 35)


def quit_game():
    pygame.quit()
    sys.exit()


# Initialize game
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
apples = []
balls = []

# Create space
space = pymunk.Space()
space.gravity = (0, 500)

# Create obstacles
balls.append(static_ball(space, (100, 400)))
balls.append(static_ball(space, (210, 500)))
balls.append(static_ball(space, (300, 300)))
balls.append(static_ball(space, (450, 400)))
balls.append(static_ball(space, (600, 300)))
balls.append(static_ball(space, (700, 450)))

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()
        if event.type == pygame.MOUSEBUTTONDOWN:
            apples.append(create_apple(space, event.pos))

    # Draw screen
    screen.fill('Black')

    # Draw elements
    draw_apples(apples)
    draw_static_balls(balls)

    # Update physics
    space.step(1/50)  # update physics
    pygame.display.update()  # update screen
    clock.tick(120)


