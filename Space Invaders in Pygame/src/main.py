import pygame
import sys
import json
from random import choice, randint

from settings import settings, update_settings
from player import Player
from alien import Alien, Extra
from laser import Laser
import obstacle


class Game:
    """All the game logic will go inside this class"""

    def __init__(self):
        # Player
        player_sprite = Player((settings["screen"]["width"] / 2, settings["screen"]["height"]))
        self.player = pygame.sprite.GroupSingle(player_sprite)

        # Health
        self.lives = settings["player"]["lives"]
        self.life_surface = pygame.image.load('../graphics/player.png').convert_alpha()
        self.lives_x_start_pos = settings["screen"]["width"] - (self.life_surface.get_width() * 2 + 30)

        # Score
        self.score = 0
        self.font = pygame.font.Font('../font/Pixeled.ttf', 20)

        # Obstacle
        self.shape = obstacle.shape
        self.block_size = settings["obstacle"]["block-size"]
        self.blocks = pygame.sprite.Group()
        self.obstacle_amount = settings["obstacle"]["quantity"]
        self.obstacle_x_positions = [num * (settings["screen"]["width"] / self.obstacle_amount) for num in range(self.obstacle_amount)]
        self.create_multiple_obstacles(45, 520, self.obstacle_x_positions)

        # Aliens
        self.aliens = pygame.sprite.Group()
        self.alien_setup(6, 8, 60, 60, 70, 60)
        # alien lasers
        self.alien_lasers = pygame.sprite.Group()
        # extra alien
        self.extra = pygame.sprite.GroupSingle()
        self.extra_spawn_time = randint(400, 800)

        # Audio
        music = pygame.mixer.Sound('../audio/music.wav')
        music.set_volume(0.2)
        music.play(loops=-1)  # play forever

        self.laser_sound = pygame.mixer.Sound('../audio/laser.wav')
        self.laser_sound.set_volume(0.5)
        self.explosion_sound = pygame.mixer.Sound('../audio/explosion.wav')
        self.explosion_sound.set_volume(0.3)

    def create_obstacle(self, x_start, y_start, offset_x):
        """ Block positioning logic per obstacle """
        for row_index, row in enumerate(self.shape):
            for col_index, col in enumerate(row):
                if col == 'x':
                    # include start position and offset
                    x = x_start + col_index * self.block_size + offset_x
                    y = y_start + row_index * self.block_size
                    block = obstacle.Block(self.block_size, 'Red', x, y)
                    self.blocks.add(block)

    def create_multiple_obstacles(self, x_start, y_start, offset_list):
        """ Number of obstacles positioned and distance between them """
        for x in offset_list:
            self.create_obstacle(x_start, y_start, x)

    def alien_setup(self, rows, cols, x_distance, y_distance, x_offset, y_offset):
        """ Position aliens on multiple rows """
        for row_index, row in enumerate(range(rows)):
            for col_index, col in enumerate(range(cols)):
                x_pos = col_index * x_distance + x_offset
                y_pos = row_index * y_distance + y_offset

                if row_index == 0:
                    alien_sprite = Alien("yellow", x_pos, y_pos)
                elif 1 <= row_index <= 2:
                    alien_sprite = Alien("green", x_pos, y_pos)
                else:
                    alien_sprite = Alien("red", x_pos, y_pos)
                self.aliens.add(alien_sprite)

    def alien_position_checker(self):
        for alien in self.aliens.sprites():
            if alien.rect.right >= settings["screen"]["width"] or alien.rect.left <= 0:
                # change direction
                settings["alien"]["movement"]["x_direction"] *= -1
                update_settings(settings)
                # move down
                self.alien_move_down(settings["alien"]["movement"]["y_drop"])
                break

    def alien_move_down(self, distance):
        if self.aliens:
            for alien in self.aliens.sprites():
                alien.rect.y += distance

    def alien_shoot(self):
        if self.aliens:
            random_alien = choice(self.aliens.sprites())
            laser_sprite = Laser(random_alien.rect.center, settings["alien"]["laser"]["speed"])
            self.alien_lasers.add(laser_sprite)
            self.laser_sound.play()

    def extra_alien_timer(self):
        self.extra_spawn_time -= 1
        if self.extra_spawn_time <= 0:
            self.extra.add(Extra(choice(['right', 'left'])))
            self.extra_spawn_time = randint(400, 800)

    def collision_checks(self):
        # Player lasers
        if self.player.sprite.lasers:
            for laser in self.player.sprite.lasers:

                # obstacle collisions
                if pygame.sprite.spritecollide(laser, self.blocks, True):
                    # destroy the laser after first block collision
                    laser.kill()
                    self.explosion_sound.play()

                # alien collissions
                aliens_hit = pygame.sprite.spritecollide(laser, self.aliens, True)  # (returns a list)
                if aliens_hit:
                    for alien in aliens_hit:
                        self.score += alien.value
                    laser.kill()
                    self.explosion_sound.play()

                # extra collision
                if pygame.sprite.spritecollide(laser, self.extra, True):
                    self.score += 500
                    laser.kill()
                    self.explosion_sound.play()

        # Alien lasers
        if self.alien_lasers:
            for laser in self.alien_lasers:

                # obstacle collisions
                if pygame.sprite.spritecollide(laser, self.blocks, True):
                    # destroy the laser after first block collision
                    laser.kill()
                    self.explosion_sound.play()

                # player collissions
                if pygame.sprite.spritecollide(laser, self.player, False):
                    laser.kill()
                    self.explosion_sound.play()
                    self.lives -= 1
                    if self.lives <= 0:
                        quit_game()

        # Aliens
        if self.aliens:
            for alien in self.aliens:

                # obstacle collisions
                pygame.sprite.spritecollide(alien, self.blocks, True)

                # player collisions
                if pygame.sprite.spritecollide(alien, self.player, False):
                    quit_game()

    def display_lives(self):
        for life in range(self.lives - 1):
            x = self.lives_x_start_pos + (life * (self.life_surface.get_width() + 15))
            screen.blit(self.life_surface, (x, 8))

    def display_score(self):
        score_surf = self.font.render(f"Score: {self.score}", True, 'White')
        score_rect = score_surf.get_rect(topleft=(10, -10))
        screen.blit(score_surf, score_rect)

    def victory_message(self):
        if not self.aliens.sprites():
            victory_surface = self.font.render("You won!", True, "white")
            victory_rect = victory_surface.get_rect(center=(settings["screen"]["width"] / 2,
                                                            settings["screen"]["height"] / 2))
            screen.blit(victory_surface, victory_rect)

    def run(self):
        # Update sprite groups
        self.player.update()  # (update player and lasers)
        self.aliens.update(settings["alien"]["movement"]["x_direction"])
        self.alien_position_checker()
        self.alien_lasers.update()  # (update alien lasers)
        self.extra_alien_timer()
        self.extra.update()  # (update extra alien)

        # check collisions
        self.collision_checks()

        # Draw sprite groups
        self.player.draw(screen)
        self.aliens.draw(screen)
        self.alien_lasers.draw(screen)
        self.extra.draw(screen)
        self.player.sprite.lasers.draw(screen)
        self.blocks.draw(screen)
        self.display_lives()
        self.display_score()
        self.victory_message()


class CRT:
    def __init__(self):
        self.tv = pygame.image.load('../graphics/tv.png').convert_alpha()
        self.tv = pygame.transform.scale(self.tv, (settings["screen"]["width"], settings["screen"]["height"]))

    def draw(self):
        self.tv.set_alpha(randint(75, 90))  # use random opacity to simulate CRT flickering
        self.create_crt_lines()
        screen.blit(self.tv, (0, 0))

    def create_crt_lines(self):
        line_height = 3
        line_amount = int(settings["screen"]["height"] / line_height)
        for line in range(line_amount):
            y_pos = line * line_height
            pygame.draw.line(self.tv, 'black', (0, y_pos), (settings["screen"]["width"], y_pos), 2)


def quit_game():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    # Initialize
    pygame.init()
    screen = pygame.display.set_mode((settings["screen"]["width"], settings["screen"]["height"]))
    clock = pygame.time.Clock()
    game = Game()
    crt = CRT()

    ALIEN_LASER = pygame.USEREVENT + 1
    pygame.time.set_timer(ALIEN_LASER, settings["alien"]["laser"]["timer"])

    while True:
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == ALIEN_LASER:
                game.alien_shoot()

        # Update and draw elements
        screen.fill((40, 40, 40))
        game.run()
        crt.draw()

        # Refresh
        pygame.display.flip()
        clock.tick(60)
