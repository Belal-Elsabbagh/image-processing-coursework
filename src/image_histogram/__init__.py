import matplotlib.pyplot as plt
import cv2


def generate_image_histogram(img):
    return cv2.calcHist([img], [0], None, [256], [0, 256])


def plot_image_histogram(img):
    plt.plot(generate_image_histogram(img))
    plt.show()
