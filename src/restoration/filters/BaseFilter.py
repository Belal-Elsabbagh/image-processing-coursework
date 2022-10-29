from abc import abstractmethod

import numpy as np

from src.img_ops import get_shape
from src.img_ops.quantize_intensity import quantize_intensity


class BaseFilter:
    window_len = 3

    def __init__(self, _img, window_len):
        if window_len % 2 == 0 or window_len < 3:
            raise Exception(f"Window length must be an odd number not less than 3. Given {window_len}")
        self.img = _img
        self.img_shape = get_shape(self.img)
        self.window_len = window_len
        self.offset = int(self.window_len / 2)
        self.row_mirror_index, self.col_mirror_index = self.init_mirror_indexes()

    @abstractmethod
    def convulse(self, pixels):
        pass

    def init_mirror_indexes(self):
        init_row, init_col, end_row, end_col = self.get_index_bounds()
        return self.get_mirror_indexes(init_row, init_col, end_row, end_col)

    def get_window(self, _row, _col):
        min_row, min_col, max_row, max_col = self.get_window_limits(_row, _col)
        return [
            [self.img[self.row_mirror_index.get(r, r)][self.col_mirror_index.get(p, p)] for p in
             range(min_col, max_col + 1)]
            for r in range(min_row, max_row + 1)
        ]

    def get_window_limits(self, _row, _col):
        """
        Returns:
             min_row, min_col, max_row, max_col
        """
        return _row - self.offset, _col - self.offset, _row + self.offset, _col + self.offset

    def get_index_bounds(self):
        return 0 - self.offset, 0 - self.offset, self.img_shape.height + self.offset, self.img_shape.width + self.offset

    def get_filtered_img(self):
        return np.array(
            [[self.convulse_point(r, p) for p in range(self.img_shape.width)] for r in range(self.img_shape.height)],
            dtype=np.uint8)

    def convulse_point(self, row_ind, pix_ind):
        return quantize_intensity(self.convulse(self.get_window(row_ind, pix_ind)))

    def get_mirror_indexes(self, _init_row, _init_col, _end_row, _end_col):
        row_mirror_index: dict = {}
        col_mirror_index: dict = {}
        for i in range(_init_row, 0):
            row_mirror_index[i] = i + self.window_len - 1
        for i in range(self.img_shape.height, _end_row):
            row_mirror_index[i] = i - self.window_len - 1
        for i in range(_init_col, 0):
            col_mirror_index[i] = i + self.window_len - 1
        for i in range(self.img_shape.width, _end_col):
            col_mirror_index[i] = i - self.window_len - 1
        return row_mirror_index, col_mirror_index
