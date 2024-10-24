import pygame

from . import InputController

class Player:
	def __init__(self, rect):
		self.rect = rect
		self.controls = InputController.InputController()

		self.y_vel = 0
		
	def update(self, surface):
		self.move()
		pygame.draw.rect(surface, (255, 0, 0), self.rect)
		
	def move(self):
		if self.controls.input_connected():
			if self.controls.left:
				self.rect.x -= 4
			if self.controls.right:
				self.rect.x += 4