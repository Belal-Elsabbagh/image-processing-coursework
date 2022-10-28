import src.img_ops
from src.img_ops import get_shape
from src.img_ops.quantize_intensity import quantize_intensity


def base_transform(img, transformation_function, *args):
    img_shape = src.img_ops.get_shape(img)
    height, width = img_shape[get_shape.HEIGHT], img_shape[get_shape.WIDTH]
    return [[quantize_intensity(transformation_function(img[row][pixel], *args)) for pixel, val in range(width)]
            for row in range(height)]
