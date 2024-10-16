import pygame, random

class Particle:
    def __init__(self, pos, image):
        self.pos = pos
        self.image = image

class ParticleGenerator:
    def __init__(self, pos, image_sequence, image_cycle_type="Randomise", concentration=10, shrink=False, generation_angle=0, min_spread_angle=-15, max_spread_angle=15, min_rand_size=1, max_rand_size=1, min_distance=10, max_distance=30):
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

        self.generate()

    def generate(self):
        for i in range(0, self.concentration):
            for img in self.image:
                image = pygame.image.load(img).convert()
                editedimage = pygame.transform.scale(image.copy(), [image.width*random.randint(self.min_rand_size, self.max_rand_size), image.height*random.randint(self.min_rand_size, self.max_rand_size)])

                particle = Particle(pos=(random.randint(50, 594), random.randint(50, 494)), image=editedimage)

                self.particle_list.append(particle)

    def show(self, surface):
        for particle in self.particle_list:
            surface.blit(particle.image, particle.pos)

