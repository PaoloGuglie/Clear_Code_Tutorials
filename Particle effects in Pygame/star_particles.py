#                   IMPORTS
import pygame
import sys
import random


#                         CLASSES
class ParticleStar:
    def __init__(self):
        self.items = []
        self.surface = pygame.image.load('star.png').convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (30, 30))
        self.width = self.surface.get_rect().width
        self.height = self.surface.get_rect().height

    # move the particles
    def emit(self):
        if self.items:
            # delete particles with radius < 0
            self.delete_particles()

            for particle in self.items:
                particle[0].x += particle[1]
                particle[0].y += particle[2]
                particle[3] -= 0.2
                # draw the star on screen
                screen.blit(self.surface, particle[0])

    # add particles
    def add_particle(self):
        pos_x = pygame.mouse.get_pos()[0] - self.width / 2
        pos_y = pygame.mouse.get_pos()[1] - self.height / 2
        direction_x = random.randint(-3, 3)
        direction_y = random.randint(-3, 3)
        lifetime = random.randint(4, 10)
        particle_rect = pygame.Rect(pos_x, pos_y, self.width, self.height)
        self.items.append([particle_rect, direction_x, direction_y, lifetime])

    # delete the particles after a certain time
    def delete_particles(self):
        items_copy = [i for i in self.items if i[3] > 0]
        self.items = items_copy


#                   FUNCTIONS
def quit_game():
    pygame.quit()
    sys.exit()


# Initialize game
pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

particles = ParticleStar()

# Custom events
PARTICLE_EVENT = pygame.USEREVENT + 1
SPAWN_TIMER_MS = 40
pygame.time.set_timer(PARTICLE_EVENT, SPAWN_TIMER_MS)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()
        if event.type == PARTICLE_EVENT:
            particles.add_particle()

    # Hide the mouse cursor
    pygame.mouse.set_visible(False)

    # Draw elements
    screen.fill('Black')
    particles.emit()

    # Update screen
    pygame.display.update()
    clock.tick(60)
