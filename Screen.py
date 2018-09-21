import time, sys
import pygame

BACKGROUND = (100, 100, 100)
BOX = (50, 50, 75)

def init(size):
    global display
    display = pygame.display.set_mode((size, size))
    pygame.display.set_caption("Map")

def update(map_class):
    global display

    display.fill(BACKGROUND)
    for r in map_class.boxes:
        pygame.draw.rect(display, BOX, r)
    pygame.display.update()
