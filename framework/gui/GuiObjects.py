import pygame

class GuiContainer:
    def __init__(self, parentSurface: pygame.Surface):
        self.surface = pygame.Surface((parentSurface.get_width(), parentSurface.get_height()))
        self.children = []

    def show(self):
        for child in self.children:
            child.show(self.surface)

class Button:
    def __init__(self, x, y, height, width, image=None, text=""):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.text = text
        self.image = image
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def show(self, surface):
        if self.image is not None:
            surface.blit(self.image, (self.x, self.y))
        elif self.image is None:
            pygame.draw.rect(surface, (255, 255, 255), self.rect)