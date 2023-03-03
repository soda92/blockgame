from blockgame.app import config

IMG = config.IMG_Dir.joinpath("2.jfif")

import pygame

pygame.init()
pygame.display.set_mode((800, 600))
image = pygame.image.load(str(IMG)).convert()
rect = image.get_rect()
screen = pygame.display.set_mode((rect.width, rect.height))

import sys

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 0, 0))
    screen.blit(image, rect)
    w = rect.width
    y_blocks = int(rect.height // (w / 4))
    for i in range(y_blocks + 1):
        pygame.draw.line(
            surface=screen,
            color=(104, 104, 104),
            start_pos=(0, i * w / 4),
            end_pos=(rect.width, i * w / 4),
            width=3,
        )
    for i in range(4 + 1):
        pygame.draw.line(
            surface=screen,
            color=(104, 104, 104),
            start_pos=(i * w / 4, 0),
            end_pos=(i * w / 4, rect.width / 4 * y_blocks),
            width=3,
        )

    pygame.display.flip()
    clock.tick(60)
