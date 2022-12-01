"""
Author: Anthony Swierkosz

Anthony's individual fingerprint minutiae extraction techniques.
"""

import cv2 as cv
from matplotlib import pyplot as plt


def load_image(image_path):
    return cv.imread(image_path, 0)


def binarize_image(image):
    """
    Converts a grayscale image into a binary image.

    :param image: Image to binarize.
    :return: Binarized image.
    """
    ret, image = cv.threshold(image, 72, 1, cv.THRESH_BINARY)

    return image


def morphological_transformation(image):
    """
    Performs a morphological transformation on the greyscale image.

    :return: The transformed image.
    """
    # Create a structuring element
    eclipse = cv.getStructuringElement(cv.MORPH_ELLIPSE, (10, 10))

    # Perform the morphological transformation
    lowest_gray = cv.morphologyEx(image, cv.MORPH_OPEN, eclipse)
    highest_gray = cv.morphologyEx(image, cv.MORPH_CLOSE, eclipse)

    # Return the intersection of the two images
    return lowest_gray + highest_gray


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
    reference_image = morphological_transformation(reference_image)
    subject_image = morphological_transformation(subject_image)

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
    from main import load_data

    main(load_data())
