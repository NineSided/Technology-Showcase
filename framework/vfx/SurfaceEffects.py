import pygame
from pygame.locals import *

# effects

def transparency(surface, transparency):
    surf = pygame.Surface((surface.get_width(), surface.get_height()))
    surf.blit(surface, (0, 0), special_flags=BLEND_RGB_ADD)

    return surf

def glow(radius, color):
    surf = pygame.Surface((radius * 2, radius * 2))
    pygame.draw.circle(surf, color, (radius, radius), radius)
    surf.set_colorkey((0, 0, 0))

    return surf