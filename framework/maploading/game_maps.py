import pygame


class Map:
    def __init__(self, DIRECTORY):
        self.DIRECTORY = DIRECTORY
        self.rawdata = open(self.DIRECTORY, "rt")
        self.gamedata = None
        self.rects = []

    def generate(self):
        MAP = []
        ROW = []

        for i in self.rawdata:
            for j in i:
                if j != "\n":
                    ROW.append(j)
            MAP.append(ROW)
            ROW = []

        self.gamedata = MAP.copy()

    def show_map(self, tileindex, surface, surfaceeffects=None, offset=None):
        surf = pygame.Surface((surface.get_width()/2, surface.get_height()/2))

        if surfaceeffects is None:
            surfaceeffects = []
        if offset is None:
            offset = [0, 0]
        y=0
        for row in self.gamedata:
            x=0
            for tile in row:
                if tile == "0":
                    pass
                if tile == "1":
                    surf.blit(tileindex[tile], (x*16+offset[0], y*16+offset[1]))
                x+=1
            y+=1

        surf_ = pygame.transform.scale(surf, (surface.get_width(), surface.get_height()))
        surf_.set_colorkey((0, 0, 0))
        return surf_

