from src.gray_level_transformations.base_transform import base_transform


def gray_level_slice_function(r, min_thr, max_thr, keep_level):
    return (r if keep_level is True else 255) if min_thr < r < max_thr else 0


def slice_gray_level(img, min_thr, max_thr, keep=False):
    return base_transform(img, gray_level_slice_function, min_thr, max_thr, keep)
