"""
Author: Anthony Swierkosz

Anthony's individual fingerprint minutiae extraction techniques.
"""

import cv2 as cv
from matplotlib import pyplot as plt

from main import load_data


def load_image(image_path):
    return cv.imread(image_path, 0)


def binarize_image(image):
    """
    Binarize an image.

    :param image: Image to binarize.
    :return: Binarized image.
    """

    # Binarize image
    ret, image = cv.threshold(image, 72, 1, cv.THRESH_BINARY)

    # Return binarized image
    return image


def main(dataset):
    """
    Main method for Anthony's individual components.

    :param dataset: Dataset to use.
    :return:
    """
    # Load images
    reference_image = load_image(dataset.training[0].reference.get_image_path())
    subject_image = load_image(dataset.training[0].subject.get_image_path())

    # Binarize images
    reference_image = binarize_image(reference_image)
    subject_image = binarize_image(subject_image)

    # Show images
    plt.subplot(121), plt.imshow(reference_image, cmap='gray')
    plt.title('Reference Image')

    plt.subplot(122), plt.imshow(subject_image, cmap='gray')
    plt.title('Subject Image')
    plt.show()


# Only if this file is run directly
if __name__ == '__main__':
    main(load_data())
