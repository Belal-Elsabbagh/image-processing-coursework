import numpy as np

from src.gray_level_transformations.base_transform import base_transform


def gamma_correction_function(r, gamma, c):
    return c * (r ** gamma)


def correct_gamma(img, gamma, c=None):
    if c is None:
        c = 255 / (np.max(img) ** gamma)
    return base_transform(img, gamma_correction_function, gamma, c)
