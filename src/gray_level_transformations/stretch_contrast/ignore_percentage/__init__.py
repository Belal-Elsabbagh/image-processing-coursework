from src.img_ops import get_shape
from src.image_histogram import generate_image_histogram


def ignore_percentage(img, percent):
    n_pixels_to_ignore = int(percent * get_shape.get_shape(img)[get_shape.PX_COUNT])
    hist = generate_image_histogram(img)
    min_quota = n_pixels_to_ignore
    min_level = 0
    for i in hist:
        min_quota -= i[0]
        if min_quota < 0:
            break
        min_level += 1
    max_quota = n_pixels_to_ignore
    max_level = 255
    for i in reversed(hist):
        max_quota -= i[0]
        if max_quota < 0:
            break
        max_level -= 1
    return min_level, max_level
