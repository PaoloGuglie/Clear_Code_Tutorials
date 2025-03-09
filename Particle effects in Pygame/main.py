import pygame
import sys


#                   CLASSES
class ParticlePrinciple:
    def __init__(self):
        self.items = []

    # move the particles
    def emit(self):
        if self.items:
            # delete particles with radius < 0
            self.delete_particles()
            for particle in self.items:
                # move
                particle[0][1] += particle[2]
                # shrink
                particle[1] -= 0.2
                # draw a circle around the particle
                pygame.draw.circle(screen, 'White',
                                   particle[0], int(particle[1]))

    # add particles
    def add_particle(self):
        pos_x = 250
        pos_y = 250
        radius = 10
        direction = -5
        particle_circle = [
            [pos_x, pos_y],
            radius,
            direction
        ]
        self.items.append(particle_circle)

    # delete the particles after a certain time
    def delete_particles(self):
        items_copy = [i for i in self.items if i[1] > 0]
        self.items = items_copy


#                   FUNCTIONS
def quit_game():
    pygame.quit()
    sys.exit()


# Initialize game
pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

particles = ParticlePrinciple()

# Custom events
PARTICLE_EVENT = pygame.USEREVENT + 1
SPAWN_TIMER_MS = 150
pygame.time.set_timer(PARTICLE_EVENT, SPAWN_TIMER_MS)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()
        if event.type == PARTICLE_EVENT:
            particles.add_particle()

    # Draw elements
    screen.fill('Black')
    particles.emit()

    # Update screen
    pygame.display.update()
    clock.tick(60)
