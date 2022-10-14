CHANNEL_COUNT = "channelCount"
WIDTH = "width"
HEIGHT = "height"


def get_shape(img):
    """
    Gets a dictionary of the image's shape
    """
    if len(img.shape) == 2:
        h, w = img.shape
        return {HEIGHT: h, WIDTH: w, CHANNEL_COUNT: 1}
    h, w, ch = img.shape
    return {HEIGHT: h, WIDTH: w, CHANNEL_COUNT: ch}
