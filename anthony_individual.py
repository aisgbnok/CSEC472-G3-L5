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

    :return: The lowest and highest greyscale values from the morphological transformation.
    """
    # Create a structuring element
    eclipse = cv.getStructuringElement(cv.MORPH_ELLIPSE, (10, 10))

    # Perform the morphological transformation
    lowest_gray = cv.morphologyEx(image, cv.MORPH_OPEN, eclipse)
    highest_gray = cv.morphologyEx(image, cv.MORPH_CLOSE, eclipse)

    # Return the lowest and highest gray values
    return lowest_gray, highest_gray


def technique_1(dataset):
    """
    Anthony's Technique 1.
    Performs a morphological transformation on the greyscale image.
    Takes the intersection of the lowest and highest greyscale values.
    Converts the greyscale image to a binary image.
    Compares the binary images using the Hamming distance.

    :param dataset: Dataset to use.
    :return: None
    """
    # Load the first image
    reference = load_image(dataset.training[10].reference.get_image_path())
    subject = load_image(dataset.training[10].subject.get_image_path())

    # Perform the morphological transformation
    reference_lowest_gray, reference_highest_gray = morphological_transformation(reference)
    subject_lowest_gray, subject_highest_gray = morphological_transformation(subject)

    # Take the intersection of the lowest and highest gray values
    # reference = cv.bitwise_xor(reference_lowest_gray, reference_highest_gray)
    # subject = cv.bitwise_xor(subject_lowest_gray, subject_highest_gray)

    # reference = reference_lowest_gray - reference_highest_gray
    # subject = subject_lowest_gray - subject_highest_gray

    intersection_reference = reference_lowest_gray + reference_highest_gray
    intersection_subject = subject_lowest_gray + subject_highest_gray

    # Binarize the images
    binary_reference = binarize_image(intersection_reference)
    binary_subject = binarize_image(intersection_subject)

    # Show images
    figure = plt.figure(constrained_layout=True)
    figure.set_size_inches(10, 16)
    figure.suptitle("Technique 1")
    (original, morph, intersection, binary) = figure.subfigures(4, 1)

    # Original
    original.suptitle("Original Images")
    (original_ref, original_sub) = original.subplots(1, 2)
    original_ref.imshow(reference, cmap='gray')
    original_ref.set_title("Reference Image")
    original_sub.imshow(subject, cmap='gray')
    original_sub.set_title("Subject Image")

    # Morphological Transformation
    morph.suptitle("Morphological Transformation")
    ((morph_ref_low, morph_sub_low), (morph_ref_high, morph_sub_high)) = morph.subplots(2, 2)
    morph_ref_low.imshow(reference_lowest_gray, cmap='gray')
    morph_ref_low.set_title("Reference Lowest Gray")
    morph_ref_high.imshow(reference_highest_gray, cmap='gray')
    morph_ref_high.set_title("Reference Highest Gray")
    morph_sub_low.imshow(subject_lowest_gray, cmap='gray')
    morph_sub_low.set_title("Subject Lowest Gray")
    morph_sub_high.imshow(subject_highest_gray, cmap='gray')
    morph_sub_high.set_title("Subject Highest Gray")

    # Intersection
    intersection.suptitle("Intersection")
    (intersection_ref, intersection_sub) = intersection.subplots(1, 2)
    intersection_ref.imshow(intersection_reference, cmap='gray')
    intersection_ref.set_title("Reference Image")
    intersection_sub.imshow(intersection_subject, cmap='gray')
    intersection_sub.set_title("Subject Image")

    # Binary
    binary.suptitle("Binary")
    (binary_ref, binary_sub) = binary.subplots(1, 2)
    binary_ref.imshow(binary_reference, cmap='gray')
    binary_ref.set_title("Reference Image")
    binary_sub.imshow(binary_subject, cmap='gray')
    binary_sub.set_title("Subject Image")

    plt.show()


def main(dataset):
    """
    Main method for Anthony's individual components.

    :param dataset: Dataset to use.
    :return: None
    """
    # Technique 1
    technique_1(dataset)


# Only if this file is run directly
if __name__ == '__main__':
    from main import load_data

    main(load_data())
