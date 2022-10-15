import numpy as np

from src.gray_level_transformations.base_transform import base_transform


def log_transform_function(r, c):
    return c * (np.log(r + 1))


def log_transform(img, c):
    return base_transform(img, log_transform_function, c)
