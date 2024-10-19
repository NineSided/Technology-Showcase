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
# CONFIG

# SETUP
clock = pygame.time.Clock()

window_size = [800, 500]
if SHADERS:
    window = pygame.display.set_mode(window_size, pygame.OPENGL | pygame.DOUBLEBUF)
elif not SHADERS:
    window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Technologies Showcase")

surface = pygame.Surface(window_size)

# MAIN
if SHADERS:
    gameplay_shader = Shaders.Shader()

g = Particles.ParticleGenerator(pos=pygame.mouse.get_pos(), p=None, color_=[random.randint(200, 255), random.randint(100, 155), 0])

while 1:
    surface.fill((0, 0, 0))

    pygame.draw.rect(surface, (255, 255, 0), pygame.Rect(50, 50, 50, 50))
    pygame.draw.rect(surface, (200, 55, 123), pygame.Rect(150, 150, 200, 350))

    g.color = [random.randint(200, 255), random.randint(100, 155), 0]

    g.pos = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        g.active = True
    elif pygame.mouse.get_pressed()[0] == False:
        g.active = False
    if pygame.mouse.get_pressed()[2]:
        g.ractive = True
    elif pygame.mouse.get_pressed()[2] == False:
        g.ractive = False
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

