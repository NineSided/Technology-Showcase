import pygame, random
from pygame.locals import *

from framework.vfx import Glow

class ParticleGenerator:
    def __init__(self, pos, p, color_=None):
        if color_ is None:
            color_ = [255, 255, 255]
        self.pos = pos

        self.particle_list = []
        self.p = p
        self.color = color_

        self.active = False
        self.ractive = False

    def generate(self, surface_):
        if self.active:
            self.particle_list.append([[self.pos[0], self.pos[1]], [random.randint(0, 20) / 10 - 1, -2], random.randint(4, 10), self.color, False])
        if self.ractive:
            self.particle_list.append([[self.pos[0], self.pos[1]], [random.randint(0, 20) / 10 - 1, -2], random.randint(4, 10), self.color, True])

        for particle in self.particle_list:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= 0.1
            particle[1][1] += 0.1

            if isinstance(self.p, pygame.Surface):
                surface_.blit(self.p, particle[0])
            else:
                pygame.draw.circle(surface_, particle[3], (int(particle[0][0]), int(particle[0][1])), int(particle[2]))

                radius = int(particle[2]*2)

                if particle[4] == True:
                    surface_.blit(Glow.create_glow(radius, (particle[3][0]/7.5, particle[3][1]/7.5, particle[3][2]/4)), (int(particle[0][0] - radius), int(particle[0][1] - radius)), special_flags=BLEND_RGB_ADD)

            if particle[2] <= 0:
                self.particle_list.remove(particle)

