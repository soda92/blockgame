from blockgame.app import config

IMG = config.IMG_Dir.joinpath("2.jfif")

import pygame

pygame.init()
pygame.display.set_mode((800, 600))
image = pygame.image.load(str(IMG)).convert()
rect = image.get_rect()
screen = pygame.display.set_mode((rect.width, rect.height))

import sys

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 0, 0))
    screen.blit(image, rect)

    pygame.display.flip()
