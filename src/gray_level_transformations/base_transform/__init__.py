import numpy as np

from src import BLACK, PEAK_INTENSITY
from src.img_ops import get_shape


def quantize(r):
    if r < BLACK:
        return BLACK
    if r > PEAK_INTENSITY:
        return PEAK_INTENSITY
    return int(r)


def base_transform(img, transformation_function, *args):
    img_shape = get_shape.get_shape(img)
    height, width = img_shape[get_shape.HEIGHT], img_shape[get_shape.WIDTH]
    new_img = np.full((height, width), BLACK, dtype=np.uint8)
    for row in range(height):
        for pixel in range(width):
            new_img[row][pixel] = quantize(transformation_function(img[row][pixel], *args))
    return new_img
