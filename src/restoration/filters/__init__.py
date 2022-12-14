from itertools import chain

import numpy as np
from scipy.stats import gmean

from src.restoration.filters import BaseFilter
from src.restoration.filters.BaseFilter import BaseFilter


class ArithmeticMeanFilter(BaseFilter):
    def __init__(self, img, window_len):
        super().__init__(img, window_len)

    def convulse(self, pixels):
        return np.mean(pixels)


class ContraharmonicMeanFilter(BaseFilter):
    exponent = 2

    def __init__(self, img, window_len, q):
        super().__init__(img, window_len)
        self.exponent = q

    @staticmethod
    def __contraharmonic_mean(_data_list, _exponent):
        return np.sum([i**(_exponent+1) for i in _data_list]) / np.sum([i ** _exponent for i in _data_list])

    def convulse(self, _pixels):
        pixels = list(chain.from_iterable(_pixels))
        return ContraharmonicMeanFilter.__contraharmonic_mean(pixels, self.exponent)


class GeometricMeanFilter(BaseFilter):
    def __init__(self, img, window_len):
        super().__init__(img, window_len)

    def convulse(self, pixels):
        return gmean(list(chain.from_iterable(pixels)))


class HarmonicMeanFilter(BaseFilter):
    def __init__(self, img, window_len):
        super().__init__(img, window_len)

    @staticmethod
    def harmonic_mean(_data_list):
        return len(_data_list) / np.sum([1/i for i in _data_list])

    def convulse(self, _pixels):
        pixels = list(chain.from_iterable(_pixels))
        return HarmonicMeanFilter.harmonic_mean(pixels)


class MaximumFilter(BaseFilter):
    def __init__(self, img, window_len):
        super().__init__(img, window_len)

    def convulse(self, pixels):
        return np.max(pixels)


class MedianFilter(BaseFilter):
    def __init__(self, img, window_len):
        super().__init__(img, window_len)

    def convulse(self, pixels):
        return np.median(pixels)


class MidpointFilter(BaseFilter):
    def __init__(self, img, window_len):
        super().__init__(img, window_len)

    def convulse(self, pixels):
        return self.get_midpoint(pixels)

    @staticmethod
    def get_midpoint(pixels):
        max_p = int(np.max(pixels))
        min_p = int(np.min(pixels))
        sum_p = max_p + min_p
        midpoint = sum_p / 2
        return midpoint


class MinimumFilter(BaseFilter):
    def __init__(self, img, window_len):
        super().__init__(img, window_len)

    def convulse(self, pixels):
        return np.min(pixels)
