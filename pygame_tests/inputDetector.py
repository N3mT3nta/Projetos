import pygame
import sys

from pygame.constants import KEYDOWN

pygame.init()
pygame.display.init()
size = 320, 240
pygame.display.set_mode(size)

keyboard = pygame.key.get_pressed()[pygame.K_SPACE]

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_SPACE:
                print('espaco apertado')