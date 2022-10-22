"""
Main module
"""

import cv2 as cv2

from src.img_ops.convert_to_grayscale import convert_to_grayscale
from src.image_histogram import plot_image_histogram
from src.img_ops.scale_img import scale_img
from src.restoration.filters.GeometricMeanFilter import GeometricMeanFilter
from src.restoration.filters.HarmonicMeanFilter import HarmonicMeanFilter
from src.restoration.filters.MaximumFilter import MaximumFilter
from src.restoration.filters.MedianFilter import MedianFilter
from src.restoration.filters.MidpointFilter import MidpointFilter
from src.restoration.filters.MinimumFilter import MinimumFilter

if __name__ == '__main__':
    img = convert_to_grayscale(cv2.imread('img/noisy_cameraman.png'))
    print(img)
    # plot_image_histogram(img)
    new_filter = MedianFilter(img, 3)
    scaled_img = new_filter.get_filtered_img()
    plot_image_histogram(scaled_img)
    cv2.imshow('test', scaled_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
