from src import BLACK, PEAK_INTENSITY
from src.gray_level_transformations.base_transform import base_transform
from src.gray_level_transformations.stretch_contrast.ignore_percentage import ignore_percentage


def contrast_stretch_function(r, r_min, r_max, s_min=0, s_max=255):
    slope = (s_max - s_min) / (r_max - r_min)
    return ((r-r_min) * slope) + s_min


def stretch_contrast(img, r_min=None, r_max=None, s_min=BLACK, s_max=PEAK_INTENSITY):
    if r_min is None and r_max is None:
        r_min, r_max = ignore_percentage(img, 0.15)
    return base_transform(img, contrast_stretch_function, r_min, r_max, s_min, s_max)
