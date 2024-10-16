import pygame, sys, math, moderngl

from pygame.locals import *

pygame.init()

from framework.moderngl import Shaders
from framework.vfx import Particles

# CONFIG

# SETUP
clock = pygame.time.Clock()

window_size = [600, 400]
window = pygame.display.set_mode(window_size, pygame.OPENGL | pygame.DOUBLEBUF)
pygame.display.set_caption("Technologies Showcase")

surface = pygame.Surface(window_size)

# MAIN
gameplay_shader = Shaders.Shader()

g = Particles.ParticleGenerator(pos=[50, 50], image_sequence=["image.bmp"], concentration=100)

while 1:
    surface.fill((0, 0, 0))

    g.show(surface)

    pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(50, 50, 50, 50))
    pygame.draw.rect(surface, (200, 55, 123), pygame.Rect(150, 150, 50, 50))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # opengl rendering
    gameplay_shader.update()

    gameplaytex = gameplay_shader.surf_to_texture(surface)
    gameplaytex.use(0)
    gameplay_shader.program['tex'] = 0
    gameplay_shader.render_object.render(mode=moderngl.TRIANGLE_STRIP)

    # framing
    pygame.display.flip()
    gameplaytex.release()
    clock.tick(60)

