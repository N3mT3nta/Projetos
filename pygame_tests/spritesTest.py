import pygame
from pygame.locals import *
from sys import exit
from os import listdir
from time import sleep

pygame.init()
size = height, width = 640, 480

screen = pygame.display.set_mode(size)
black = (0, 0, 0)

pygame.display.set_caption('spritesTest')


class Frog(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        path = 'sprites/frog/'
        filesList = listdir(path)
        filesList.sort()
        for sprite in filesList:
            self.sprites.append(pygame.image.load(path + sprite))
        self.current = 0
        self.image = self.sprites[self.current]
        self.image = pygame.transform.scale(self.image, (128*2, 64*2))
        self.rect = self.image.get_rect()
        self.rect.center = height/2, width/2

    def update(self):
        self.current += 1
        if self.current == len(self.sprites):
            self.current = 0
            self.image = self.sprites[self.current]
            self.rect = self.image.get_rect()
            self.rect.center = height/2, width/2


frog = Frog()
everySprite = pygame.sprite.Group()
everySprite.add(frog)

while True:
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    everySprite.draw(screen)
    everySprite.update()
    pygame.display.flip()
    frog.update()
