import pygame


class Weapon(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)
        self.direction = player.status.split('_', 1)[0]

        # Graphics
        self.image = pygame.Surface((40, 40))

        # Placement
        self.rect = self.image.get_rect(center=player.rect.center)
