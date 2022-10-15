CHANNEL_COUNT = "channelCount"
WIDTH = "width"
HEIGHT = "height"
PX_COUNT = 'pixelCount'


def get_shape(img):
    """
    Gets a dictionary of the image's shape
    """
    if len(img.shape) == 2:
        h, w = img.shape
        px_count = h * w
        return {HEIGHT: h, WIDTH: w, CHANNEL_COUNT: 1, PX_COUNT: px_count}
    h, w, ch = img.shape
    px_count = h * w
    return {
        HEIGHT: h,
        WIDTH: w,
        CHANNEL_COUNT: ch,
        PX_COUNT: px_count,
    }
