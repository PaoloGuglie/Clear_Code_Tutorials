import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 300))
clock = pygame.time.Clock()

# Add a background to 'cover' multiple draws of moving objects
background = pygame.image.load('../graphics/Sky.png')

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw background on screen
    screen.blit(background, (0, 0))

    # Draw a line to the screen
    pygame.draw.line(screen, 'Gold', (0, 0), (800, 300), 20)

    # Draw a mouse-following line
    pygame.draw.line(screen, 'Blue', (0, 0), pygame.mouse.get_pos(), 10)

    # Draw a circle to the screen (creating a rect inside the method)
    pygame.draw.ellipse(screen, 'Brown', pygame.Rect(50, 200, 100, 100))

    pygame.display.update()
    clock.tick(60)

