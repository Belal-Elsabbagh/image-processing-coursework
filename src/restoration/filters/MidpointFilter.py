from src.restoration.filters.BaseFilter import BaseFilter


class MidpointFilter(BaseFilter):
    def __init__(self, img, window_len):
        super().__init__(img, window_len)

    def get_corrected_pixel_value(self, row, col):
        pixels = self.get_pixels_in_window(row, col)
        return (min(pixels) + max(pixels))/2
