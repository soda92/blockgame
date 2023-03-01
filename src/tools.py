import pygame


def pil_to_surface(pil_image):
    return pygame.image.fromstring(
        pil_image.tobytes(), pil_image.size, pil_image.mode
    ).convert()


def cut_image(image_name: str, x_splits) -> list[pygame.surface.Surface]:
    from PIL import Image

    img = Image.open(image_name)
    image_sequences = []
    pieces_width = img.width / x_splits
    y_splits = int(img.height / pieces_width) - 1
    pieces_height = img.height / y_splits

    total_pieces = x_splits * y_splits
    for i in range(total_pieces):
        x_index = i % x_splits
        y_index = i // y_splits
        box = (
            x_index * pieces_width,
            y_index * pieces_height,
            (x_index + 1) * pieces_width,
            (y_index + 1) * pieces_height,
        )
        part = img.crop(box)
        image_sequences.append((pil_to_surface(part), box))
    return image_sequences
