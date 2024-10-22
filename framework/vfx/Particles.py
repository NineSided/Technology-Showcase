import pygame, random, math
from pygame.locals import *

from framework.vfx import SurfaceEffects

class ParticleGenerator:
    def __init__(self, pos, color_=None, decay_rate=0.1, direction=0, mspeed=1, gravity=0.1, spread=30, min_size=4, max_size=10, surfaceeffects=[]):
        if color_ is None:
            color_ = [255, 255, 255]
        self.pos = pos

        self.particle_list = []
        self.color = color_
        self.decay_rate = decay_rate
        self.direction = math.radians(direction-90)
        self.mspeed = mspeed
        self.gravity = gravity
        self.spread = spread
        self.min_size = min_size
        self.max_size = max_size
        self.surfaceeffects = surfaceeffects

        self.active = False

    def generate(self, surface_):
        if self.active:
            self.particle_list.append([[self.pos[0], self.pos[1]], [math.cos(self.direction+math.radians(random.randint(0, int(self.spread))-int(self.spread/2)))*self.mspeed, math.sin(self.direction+math.radians(random.randint(0, int(self.spread))-int(self.spread/2)))*self.mspeed], random.randint(self.min_size, self.max_size), self.color])

        for particle in self.particle_list:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= self.decay_rate
            particle[1][1] += self.gravity

            pygame.draw.circle(surface_, particle[3], (int(particle[0][0]), int(particle[0][1])), int(particle[2]))
            radius = int(particle[2]*2)

            if len(self.surfaceeffects) > 0 and isinstance(self.surfaceeffects, list):
                for effect in self.surfaceeffects:
                    # post-processing
                    if effect[0] == SurfaceEffects.glow:
                        surface_.blit(effect[0](eval(str(effect[1])), effect[2]), (int(particle[0][0] - eval(str(effect[1]))), int(particle[0][1] - eval(str(effect[1])))), special_flags=BLEND_RGB_ADD)

            if particle[2] <= 0:
                self.particle_list.remove(particle)

