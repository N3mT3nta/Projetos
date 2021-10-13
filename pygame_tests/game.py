import pygame
import sys

from pygame.constants import K_DOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_UP, KEYDOWN

size = width, height = 640, 480
color = pygame.Color(35, 23, 70)

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Jogo do Samuel')

#cable = pygame.image.load('cable.png')
#cableRect = cable.get_rect()
x = y = 0
clock = pygame.time.Clock()

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit()
            if event.key == K_LEFT or event.key == pygame.K_a:
                x -= 40
            if event.key == K_RIGHT or event.key == pygame.K_d:
                x += 40
            if event.key == K_UP or event.key == pygame.K_w:
                y -= 40
            if event.key == K_DOWN or event.key == pygame.K_s:
                y += 40

    screen.fill((12, 72, 167))
    obj = pygame.draw.rect(screen, color, (x, y, 50, 50))
    x += 1
    y += 1
    if x == width: x = 0
    if y == height: y = 0
    pygame.display.update()
