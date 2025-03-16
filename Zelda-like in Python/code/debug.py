import pygame

pygame.init()
font = pygame.font.Font(None, 30)


def debug(info, y=10, x=10):
    # get the display surface
    display_surface = pygame.display.get_surface()
    # get a surface and rectangle to show debug info in
    debug_surface = font.render(str(info), True, 'White')
    debug_rect = debug_surface.get_rect(topleft=(x, y))
    # draw the debug rect over the game display
    pygame.draw.rect(display_surface, 'Black', debug_rect)
    # put the debug surface over the debug rect
    display_surface.blit(debug_surface, debug_rect)
