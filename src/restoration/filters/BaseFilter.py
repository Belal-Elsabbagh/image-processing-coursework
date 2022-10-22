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

    def get_pixels_in_window(self, _row, _col):
        img_shape = get_shape.get_shape(self.img)
        img_height, img_width = img_shape[get_shape.HEIGHT], img_shape[get_shape.WIDTH]
        offset = int(self.window_len / 2)
        min_row, min_col, max_row, max_col = self.get_window_limits(_row, _col, offset)
        pixels = [
            [self.img[self.get_mirrored_index(img_height, row)][self.get_mirrored_index(img_width, pix)]
             for pix in range(min_col, max_col + 1)]
            for row in range(min_row, max_row + 1)
        ]
        return list(chain.from_iterable(pixels))

    @staticmethod
    def get_window_limits(_row, _col, offset):
        """
        Returns:
             min_row, min_col, max_row, max_col
        """
        return _row - offset, _col - offset, _row + offset, _col + offset

    def get_mirrored_index(self, img_dim, ind):
        return ind + self.window_len - 1 if ind < 0 else (ind - self.window_len - 1 if ind >= img_dim else ind)

    def get_corrected_pixel_value(self, row, col):
        pixels = self.get_pixels_in_window(row, col)
        return np.mean(pixels)

    def get_filtered_img(self):
        img = [[self.get_corrected_pixel_value(row_ind, pix_ind) for pix_ind, pix_val in enumerate(self.img[row_ind])]
               for row_ind, row_val in enumerate(self.img)]
        return np.array(img, dtype=np.uint8)
