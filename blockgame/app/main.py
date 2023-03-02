import sys
import pygame

from . import tools
from . import config

def main():
    pygame.init()
    picrect = pygame.image.load(config.IMG_Path).get_rect()
    screen = pygame.display.set_mode((picrect.width, picrect.height))

    black = 0, 0, 0
    image_sequences = tools.cut_image(config.IMG_Path, config.X_Splits)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(black)
        for image, box in image_sequences:
            screen.blit(image, box)

        pygame.display.flip()
