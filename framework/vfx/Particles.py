import pygame, random
import copy as COPY

class Particle:
    def __init__(self, pos, image):
        self.pos = pos
        self.image = image
        self.angle = 0

class ParticleGenerator:
    def __init__(self, pos, image_sequence, image_cycle_type="Randomise", concentration=10, shrink=False, generation_angle=0, min_spread_angle=-15, max_spread_angle=15, min_rand_size=1, max_rand_size=1, min_distance=10, max_distance=30, min_rot_speed=0, max_rot_speed=0):
        self.pos = pos

        self.particle_list = []
        self.image = image_sequence
        self.image_cycle_type = image_cycle_type

        self.shrink = shrink
        self.concentration = concentration

        self.generation_angle = generation_angle

        self.min_spread_angle = min_spread_angle
        self.max_spread_angle = max_spread_angle

        self.min_rand_size = min_rand_size
        self.max_rand_size = max_rand_size

        self.min_distance = min_distance
        self.max_distance = max_distance

        self.min_rot_speed = min_rot_speed
        self.max_rot_speed = max_rot_speed

        self.generate()

    def generate(self):
        for i in range(0, self.concentration):
            for img in self.image:
                particle = Particle(pos=(self.pos[0], self.pos[1]), image=img)
                self.particle_list.append(particle)

    def show(self, surface):
        for particle in self.particle_list:
            copy = particle.image
            particle.angle -= 5
            surf = pygame.transform.rotate(copy, particle.angle)
            surf2 = pygame.transform.scale(surf, (particle.image.width*2, particle.image.height*2))
            surface.blit(surf2, [particle.pos[0]-int(copy.get_width()/2), particle.pos[1]-int(copy.get_height()/2)])
