import sys
import pygame
from pygame.constants import KEYDOWN, K_SPACE

pygame.mixer.init()

pygame.display.init()

size = 900, 600

screen = pygame.display.set_mode(size)

filePath = '/home/samuel/Documentos/Scripts/Projetos/pygame_tests/music by scott nice.mp3'

pygame.display.set_caption('music player by Samuel Gomes')

music = pygame.mixer.Sound(filePath)
music.play()
pausado = False
vitrola = pygame.image.load('vitrola.png')
vitrolaRect = vitrola.get_rect()

duration = music.get_length()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == KEYDOWN and event.key == K_SPACE and not pausado:
            pygame.mixer.pause()
            pausado = True
        elif event.type == KEYDOWN and event.key == K_SPACE:
            pygame.mixer.unpause()
            pausado = False

    screen.blit(vitrola, vitrolaRect)
    pygame.display.flip()
