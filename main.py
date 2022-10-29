"""
Main module
"""

from timeit import default_timer as timer

import cv2 as cv2

from src.image_histogram import plot_image_histogram
from src.img_ops import read_img_grayscale
from src.img_ops.scale_img import resize_img
from src.restoration.filters import *

if __name__ == '__main__':
    img_path = 'img/noise.png'
    img = read_img_grayscale(img_path)
    print(img)
    plot_image_histogram(f"{img_path} before", img)
    new_filter = ContraharmonicMeanFilter(img, 3, 1)
    start = timer()
    img = new_filter.get_filtered_img()
    end = timer()
    print(f'Time elapsed: {end - start} seconds')
    plot_image_histogram(f"{img_path} after", img)
    cv2.imshow('test', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
