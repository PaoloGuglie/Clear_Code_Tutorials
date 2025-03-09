import pygame
import sys
import random


#                   CLASSES
class ParticleNyan:
    def __init__(self):
        self.items = []
        self.size = 12

    # move the particles
    def emit(self):
        if self.items:
            # delete particles with radius < 0
            self.delete_particles()
            for particle in self.items:
                # move
                particle[0].x -= 1
                # draw a circle around the particle
                pygame.draw.rect(screen, particle[1], particle[0])

        # Draw cat
        self.draw_nyan_cat()

    # add particles
    def add_particle(self, offset, color):
        pos_x = pygame.mouse.get_pos()[0]
        pos_y = pygame.mouse.get_pos()[1] + offset
        particle_rect = pygame.Rect(
            pos_x - self.size / 2,
            pos_y - self.size / 2,
            self.size, self.size
        )
        self.items.append((particle_rect, color))

    # delete the particles after a certain time
    def delete_particles(self):
        items_copy = [i for i in self.items if i[0].x > 0]
        self.items = items_copy

    def draw_nyan_cat(self):
        nyan_rect = nyan_surface.get_rect(center=pygame.mouse.get_pos())
        screen.blit(nyan_surface, nyan_rect)


#                   FUNCTIONS
def quit_game():
    pygame.quit()
    sys.exit()


# Initialize game
pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

# Nyan cat
nyan_surface = pygame.image.load('nyan_cat.png').convert_alpha()
nyan_surface = pygame.transform.scale(nyan_surface, (150, 100))

particles = ParticleNyan()

# Custom events
PARTICLE_EVENT = pygame.USEREVENT + 1
SPAWN_TIMER_MS = 40
pygame.time.set_timer(PARTICLE_EVENT, SPAWN_TIMER_MS)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()
        if event.type == PARTICLE_EVENT:
            particles.add_particle(-30, 'Red')
            particles.add_particle(-18, 'Orange')
            particles.add_particle(-6, 'Yellow')
            particles.add_particle(6, 'Green')
            particles.add_particle(18, 'Blue')
            particles.add_particle(30, 'Purple')

    # Hide the mouse cursor
    pygame.mouse.set_visible(False)

    # Draw elements
    screen.fill('Black')
    particles.emit()

    # Update screen
    pygame.display.update()
    clock.tick(60)
