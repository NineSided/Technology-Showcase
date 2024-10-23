SHADERS = True

import pygame, sys, math, random

if SHADERS:
    try:
        import moderngl
    except:
        pass

from pygame.locals import *

pygame.init()

if SHADERS:
    from framework.moderngl import Shaders

from framework.vfx import Particles
from framework.vfx import SurfaceEffects
from framework.maploading import game_maps
# CONFIG

# SETUP
clock = pygame.time.Clock()

window_size = [832, 512]
if SHADERS:
    window = pygame.display.set_mode(window_size, pygame.OPENGL | pygame.DOUBLEBUF)
elif not SHADERS:
    window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Technologies Showcase")

surface = pygame.Surface(window_size)

# MAIN
if SHADERS:
    gameplay_shader = Shaders.Shader()

g = Particles.ParticleGenerator(pos=pygame.mouse.get_pos(), color_=(200, 200, 255), decay_rate=0.1, direction=0, mspeed=1, gravity=0.1, spread=90, min_size=4, max_size=10, surfaceeffects=[[SurfaceEffects.glow, "radius", (20, 20, 80)]])
g.active = True

tile_index = {"0": None,
              "1": pygame.image.load("brick.bmp").convert()}

MAP = game_maps.Map("map.txt")
MAP.generate()

while 1:
    surface.fill((0, 0, 0))

    pygame.draw.rect(surface, (255, 255, 0), pygame.Rect(50, 50, 50, 50))
    pygame.draw.rect(surface, (200, 55, 123), pygame.Rect(150, 150, 200, 350))

    mapsurf = MAP.show_map(tile_index, surface)
    surface.blit(mapsurf, (0, 0))

    g.pos = [125, 125]
    g.generate(surface)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # rendering
    if SHADERS:
        try:
            gameplay_shader.update()

            gameplaytex = gameplay_shader.surf_to_texture(surface)
            gameplaytex.use(0)
            gameplay_shader.program['tex'] = 0
            gameplay_shader.render_object.render(mode=moderngl.TRIANGLE_STRIP)
        except:
            window.blit(surface, (0, 0))
    elif not SHADERS:
        window.blit(surface, (0, 0))

    # framing
    pygame.display.flip()
    if SHADERS:
        try:
            gameplaytex.release()
        except:
            pass
    clock.tick(60)

