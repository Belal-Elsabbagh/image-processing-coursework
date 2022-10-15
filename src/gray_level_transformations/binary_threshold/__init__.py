from src import BLACK
from src.gray_level_transformations import gray_level_slice_function
from src.gray_level_transformations.base_transform import base_transform
from src.gray_level_transformations.negative_transform import negative_transform


def binary_threshold(img, thr):
    return base_transform(img, gray_level_slice_function, BLACK, thr, False)


def inverse_binary_threshold(img, thr):
    return base_transform(negative_transform(img), gray_level_slice_function, BLACK, thr, False)
