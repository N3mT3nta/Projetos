import pygame
from os import listdir, getcwd
from sys import exit
from pygame.constants import KEYDOWN, QUIT

pygame.init()
tela = pygame.display.set_mode((640, 480))

pygame.display.set_caption('Sprites do Cable')
path = f'{getcwd()}/sprites/cable/'

filesList = listdir(path)

filesList.sort()
CurrentSprite = 0
sprite = pygame.image.load(path + filesList[CurrentSprite])
spriteRect = sprite.get_rect()

relogio = pygame.time.Clock()

while True:
    relogio.tick(16)
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    tela.fill((0, 0, 0))
    tela.blit(sprite, spriteRect)
    CurrentSprite += 1
    if CurrentSprite > len(filesList) - 1:
        CurrentSprite = 0
    sprite = pygame.image.load(path + filesList[CurrentSprite])
#    sprite = pygame.transform.scale(sprite, (640*2, 480*2))
    spriteRect = sprite.get_rect()

    pygame.display.flip()
