"""
Main module
"""

import cv2 as cv2
from convert_to_grayscale import convert_to_grayscale
from scale_img import scale_img
from gray_level_transformations import negative_transform, log_transform, gamma_correction, gray_level_slice

if __name__ == '__main__':
    img = convert_to_grayscale(cv2.imread('img/grayscale_spectrum.png'))
    print(img)
    scaled_img = scale_img(img, 1)
    scaled_img = gray_level_slice(scaled_img, 30, 60)
    cv2.imshow('test', scaled_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
