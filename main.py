"""
Main module
"""

import cv2 as cv2

from src.img_ops.convert_to_grayscale import convert_to_grayscale
from src.image_histogram import plot_image_histogram
from src.img_ops.scale_img import scale_img
from src.gray_level_transformations import slice_gray_level

if __name__ == '__main__':
    img = convert_to_grayscale(cv2.imread('img/port.jpg'))
    print(img)
    scaled_img = scale_img(img, 0.4)
    plot_image_histogram(scaled_img)
    scaled_img = slice_gray_level.slice_gray_level(scaled_img, 140, 190, True)
    plot_image_histogram(scaled_img)
    cv2.imshow('test', scaled_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
