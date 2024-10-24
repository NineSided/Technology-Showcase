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

g = Particles.ParticleGenerator(pos=[125, 125], color_=(200, 200, 255), decay_rate=0.1, direction=0, mspeed=1, gravity=0.1, spread=90, min_size=4, max_size=10, surfaceeffects=[[SurfaceEffects.glow, "radius", (20, 20, 80)], [SurfaceEffects.glow, "radius*1.5", (20, 20, 80)]])
g.active = True

tile_index = {"0": None,
              "1": pygame.image.load("brick.bmp").convert()}

MAP = Game_maps.Map("map.txt")
MAP.generate()

player = Player.Player(rect=pygame.Rect(300, 100, 25, 50))
k_a = False
k_d = False

pauseguicontainer = GuiObjects.GuiContainer(pygame.Surface((window_size[0]/2, window_size[1]/2)))

gameguicontainer = GuiObjects.GuiContainer(pygame.Surface((window_size[0]/2, window_size[1]/2)))
gameguicontainer.children["moveleft"] = GuiObjects.Button(50, 400, 100, 100, name="moveleft")
gameguicontainer.children["moveright"] = GuiObjects.Button(200, 400, 100, 100, name="moveright")

while 1:
    surface.fill((0, 0, 0))
    gameguicontainer.surface.set_colorkey((0, 0, 0))

    pygame.draw.rect(surface, (255, 255, 0), pygame.Rect(50, 50, 50, 50))
    pygame.draw.rect(surface, (200, 55, 123), pygame.Rect(150, 150, 200, 350))

    mapsurf = MAP.show_map(tile_index, surface)
    surface.blit(mapsurf, (0, 0))

    player.controls.left = gameguicontainer.children["moveleft"].rect.collidepoint(
        (pygame.mouse.get_pos()[0] / 2, pygame.mouse.get_pos()[1] / 2)) and pygame.mouse.get_pressed()[0] or k_a
    player.controls.right = gameguicontainer.children["moveright"].rect.collidepoint(
        (pygame.mouse.get_pos()[0] / 2, pygame.mouse.get_pos()[1] / 2)) and pygame.mouse.get_pressed()[0] or k_d

    g.generate()
    g.show(surface)

    player.update(surface)

    gameguicontainer.show()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                k_a = True
            if event.key == K_d:
                k_d = True
        if event.type == KEYUP:
            if event.key == K_a:
                k_a = False
            if event.key == K_d:
                k_d = False

    # rendering
    surface.blit(gameguicontainer.surface, (0, 0))
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

