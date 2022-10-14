import numpy as np
import get_shape
from gray_level_transformations.gamma_correction_function import gamma_correction_function
from gray_level_transformations.gray_level_slice_function import gray_level_slice_function
from gray_level_transformations.log_transform_function import log_transform_function
from gray_level_transformations.negative_transformation_function import negative_transformation_function


def quantize(r):
    if r < 0:
        return 0
    if r > 255:
        return 255
    return int(r)


def base_transform(img, transformation_function, *args):
    img_shape = get_shape.get_shape(img)
    height, width = img_shape[get_shape.HEIGHT], img_shape[get_shape.WIDTH]
    new_img = np.full((height, width), 0, dtype=np.uint8)
    for row in range(len(img)):
        for pixel in range(len(img[row])):
            new_img[row][pixel] = quantize(transformation_function(img[row][pixel], *args))
    return new_img


def negative_transform(img):
    return base_transform(img, negative_transformation_function)


def log_transform(img, c):
    return base_transform(img, log_transform_function, c)


def gamma_correction(img, gamma, c=None):
    if c is None:
        c = 255 / (np.max(img) ** gamma)
    return base_transform(img, gamma_correction_function, gamma, c)


def gray_level_slice(img, min_thr, max_thr, keep=False):
    return base_transform(img, gray_level_slice_function, min_thr, max_thr, keep)
