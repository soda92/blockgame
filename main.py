import sys
import random
import pygame


def pil_to_surface(pil_image):
    return pygame.image.fromstring(
        pil_image.tobytes(), pil_image.size, pil_image.mode
    ).convert()


def cut_image(image_name: str, x_num) -> list[pygame.surface.Surface]:
    from itertools import product
    from PIL import Image

    img = Image.open(image_name)
    image_sequences = []
    pieces_width = img.width / x_num
    num_height_splits = int(img.height / pieces_width)
    pieces_height = img.height / num_height_splits

    grid = product(range(0, x_num), range(0, num_height_splits))
    for i, j in grid:
        box = (
            i * pieces_width,
            j * pieces_height,
            (i + 1) * pieces_width,
            (j + 1) * pieces_height,
        )
        part = img.crop(box)
        image_sequences.append(pil_to_surface(part))
    return image_sequences, (pieces_width, pieces_height)


if __name__ == "__main__":
    pygame.init()
    IMG_name = "girl.jpeg"
    X_splits = 4
    picrect = pygame.image.load(IMG_name).get_rect()
    screen = pygame.display.set_mode((picrect.width, picrect.height))

    black = 0, 0, 0
    image_sequences, (pieces_width, pieces_height) = cut_image(IMG_name, X_splits)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(black)
        for i, s in enumerate(image_sequences):
            point = i / X_splits * pieces_height, i % X_splits + pieces_width
            area = point[0], point[1], point[0] + pieces_width, point[1] + pieces_height
            screen.blit(s, area)

        pygame.display.flip()
