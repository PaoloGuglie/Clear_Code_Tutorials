import pygame


class Block(pygame.sprite.Sprite):
    def __init__(self, size, color, pos_x, pos_y):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(pos_x, pos_y))


# I will create a block only where there is an 'x'.
shape = [
    '  xxxxxxx',
    ' xxxxxxxxx',
    'xxxxxxxxxxx',
    'xxxxxxxxxxx',
    'xxxxxxxxxxx',
    'xxx     xxx',
    'xx       xx']
