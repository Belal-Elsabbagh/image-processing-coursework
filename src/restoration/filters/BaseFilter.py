from abc import abstractmethod

import numpy as np

import src.img_ops
from src.img_ops import get_shape
from src.img_ops.quantize_intensity import quantize_intensity


class BaseFilter:
    window_len = 3

    def __init__(self, _img, window_len):
        if window_len % 2 == 0 or window_len < 3:
            raise Exception(f"Window length must be an odd number not less than 3. Given {window_len}")
        self.img = _img
        img_shape = src.img_ops.get_shape(self.img)
        self.img_height, self.img_width = img_shape.height, img_shape.width
        self.window_len = window_len
        self.offset = int(self.window_len / 2)
        self.mirror_index = self.init_mirror_indexes()

    @abstractmethod
    def convulse(self, pixels):
        pass

    def init_mirror_indexes(self):
        init_index, end_index = self.get_index_bounds()
        return self.get_mirror_indexes(init_index, end_index)

    def get_window(self, _row, _col):
        min_row, min_col, max_row, max_col = self.get_window_limits(_row, _col)
        return [
            [self.img[self.mirror_index.get(r, r)][self.mirror_index.get(p, p)] for p in range(min_col, max_col + 1)]
            for r in range(min_row, max_row + 1)
        ]

    def get_window_limits(self, _row, _col):
        """
        Returns:
             min_row, min_col, max_row, max_col
        """
        return _row - self.offset, _col - self.offset, _row + self.offset, _col + self.offset

    def get_index_bounds(self):
        return 0 - self.offset, self.img_height + self.offset

    def get_filtered_img(self):
        return np.array([[self.convulse_point(r, p) for p in range(self.img_width)] for r in range(self.img_height)],
                        dtype=np.uint8)

    def convulse_point(self, row_ind, pix_ind):
        return quantize_intensity(self.convulse(self.get_window(row_ind, pix_ind)))

    def get_mirror_indexes(self, _init_index, _end_row):
        mirror_index: dict = {}
        for i in range(_init_index, 0):
            mirror_index[i] = i + self.window_len - 1
        for i in range(self.img_height, _end_row):
            mirror_index[i] = i - self.window_len - 1
        return mirror_index
