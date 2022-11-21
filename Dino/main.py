import pygame
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((640, 240))


diiino = []
dino_img = pygame.image.load("d1.png")
dino_img.convert()
diiino.append(dino_img)

dino_img = pygame.image.load("d2.png")
dino_img.convert()
diiino.append(dino_img)

dino_img = pygame.image.load("d3.png")
dino_img.convert()
diiino.append(dino_img)



class Dino():
	def __init__(self,no):
		self.no = no
		self.image_sprite = diiino

rect=dino_img.get_rect()
rect.center = 640//2,240//2
running = True

d1 = Dino(1)
q=0

while running:
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False
	q+=1
	if q == 3:
		q=0

	screen.blit(d1.image_sprite[q],rect)
	pygame.display.update()
