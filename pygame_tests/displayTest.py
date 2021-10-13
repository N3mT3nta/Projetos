import sys
import pygame
from pygame import display

pygame.init()

size = width, height = 640, 480
screen = pygame.display.set_mode(size)
displayDriver = display.get_driver()
display.set_caption('Display do Samel')

print(f'current display driver: {displayDriver}')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
