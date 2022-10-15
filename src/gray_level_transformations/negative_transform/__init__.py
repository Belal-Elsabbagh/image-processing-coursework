from src.gray_level_transformations.base_transform import base_transform
from src import PEAK_INTENSITY


def negative_transformation_function(r):
    return PEAK_INTENSITY - r


def negative_transform(img):
    return base_transform(img, negative_transformation_function)
