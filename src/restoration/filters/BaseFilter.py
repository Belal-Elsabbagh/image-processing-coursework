from itertools import chain

import numpy as np

from src.img_ops import get_shape


class BaseFilter:
    window_len = 3

    def __init__(self, img, window_len):
        if window_len % 2 == 0 or window_len < 3:
            raise Exception(f"Window length must be an odd number not less than 3. Given {window_len}")
        self.img = img
        self.window_len = window_len

    def get_pixels_in_window(self, row_param, col_param):
        img_shape = get_shape.get_shape(self.img)
        img_height, img_width = img_shape[get_shape.HEIGHT], img_shape[get_shape.WIDTH]
        offset = int(self.window_len/2)
        min_row, min_col = row_param - offset, col_param - offset
        max_row, max_col = row_param + offset, col_param + offset
        pixels = []
        for row in range(min_row, max_row + 1):
            row = self.get_mirrored_index(img_height, row)
            new_row = [self.img[row][self.get_mirrored_index(img_width, pix)] for pix in range(min_col, max_col + 1)]
            pixels.append(new_row)
        return list(chain.from_iterable(pixels))

    def get_mirrored_index(self, img_dim, ind):
        return ind + self.window_len - 1 if ind < 0 else (ind - self.window_len - 1 if ind >= img_dim else ind)

    def get_corrected_pixel_value(self, row, col):
        pixels = self.get_pixels_in_window(row, col)
        return np.mean(pixels)

    def get_filtered_img(self):
        img_rows = enumerate(self.img)
        img = [[self.get_corrected_pixel_value(row_ind, pix_ind) for pix_ind, pix_val in enumerate(self.img[row_ind])]
               for row_ind, row_val in img_rows]
        return np.array(img, dtype=np.uint8)
