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
from framework.maploading import Game_maps
from framework.player import Player
from framework.gui import GuiObjects

# CONFIG

# SETUP
clock = pygame.time.Clock()

window_size = [1664, 1024]
if SHADERS:
    window = pygame.display.set_mode(window_size, pygame.OPENGL | pygame.DOUBLEBUF)
elif not SHADERS:
    window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Technologies Showcase")

surface = pygame.Surface((window_size[0]/2, window_size[1]/2))

# MAIN
if SHADERS:
    gameplay_shader = Shaders.Shader()
    gui_shader = Shaders.Shader()

g = Particles.ParticleGenerator(pos=pygame.mouse.get_pos(), color_=(200, 200, 255), decay_rate=0.1, direction=0, mspeed=1, gravity=0.1, spread=90, min_size=4, max_size=10, surfaceeffects=[[SurfaceEffects.glow, "radius", (20, 20, 80)], [SurfaceEffects.glow, "radius*1.5", (20, 20, 80)]])
g.active = True

tile_index = {"0": None,
              "1": pygame.image.load("brick.bmp").convert()}

MAP = Game_maps.Map("map.txt")
MAP.generate()

player = Player.Player(rect=pygame.Rect(300, 100, 25, 50))

guicontainer = GuiObjects.GuiContainer(pygame.Surface((window_size[0]/2, window_size[1]/2)))
guicontainer.children.append(GuiObjects.Button(100, 100, 100, 100))

while 1:
    surface.fill((0, 0, 0))
    guicontainer.surface.set_colorkey((0, 0, 0))

    pygame.draw.rect(surface, (255, 255, 0), pygame.Rect(50, 50, 50, 50))
    pygame.draw.rect(surface, (200, 55, 123), pygame.Rect(150, 150, 200, 350))

    mapsurf = MAP.show_map(tile_index, surface)
    surface.blit(mapsurf, (0, 0))

    player.controls.left = guicontainer.children[0].rect.collidepoint((pygame.mouse.get_pos()[0]/2, pygame.mouse.get_pos()[1]/2)) and pygame.mouse.get_pressed()[0]

    #player.controls.right = rightrect.collidepoint((pygame.mouse.get_pos()[0]/2, pygame.mouse.get_pos()[1]/2)) and pygame.mouse.get_pressed()[0]

    g.generate(surface)
    player.update(surface)

    guicontainer.show()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                player.controls.left = True
            if event.key == K_d:
                player.controls.right = True
        if event.type == KEYUP:
            if event.key == K_a:
                player.controls.left = False
            if event.key == K_d:
                player.controls.right = False

    # rendering
    surface.blit(guicontainer.surface, (0, 0))
    surf = pygame.transform.scale(surface, window_size)
    
    if SHADERS:
        try:
            gameplay_shader.update()
            gameplaytex = gameplay_shader.surf_to_texture(surf)
            gameplaytex.use(0)
            gameplay_shader.program['tex'] = 0
            gameplay_shader.render_object.render(mode=moderngl.TRIANGLE_STRIP)
        except:
            window.blit(surf, (0, 0))
    elif not SHADERS:
        window.blit(surf, (0, 0))

    # framing
    pygame.display.flip()
    if SHADERS:
        try:
            gameplaytex.release()
        except:
            pass
    clock.tick(60)

