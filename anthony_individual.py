"""
Author: Anthony Swierkosz

Anthony's individual fingerprint minutiae extraction techniques.
"""

import cv2 as cv
from matplotlib import pyplot as plt


def load_image(image_path):
    return cv.imread(image_path, 0)


def binarize_image(image, method=cv.THRESH_BINARY):
    """
    Converts a grayscale image into a binary image.

    :param image: Image to binarize.
    :param method: Method to use for binarization.
    :return: Binarized image.
    """
    ret, image = cv.threshold(image, 72, 1, method)

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

    # Go through each image in the dataset

    distances = []

    for image_pair in dataset.training:
        # Load the first image
        reference = load_image(image_pair.reference.get_image_path())
        subject = load_image(image_pair.subject.get_image_path())

        # Perform the morphological transformation
        reference_lowest_gray, reference_highest_gray = morphological_transformation(reference)
        subject_lowest_gray, subject_highest_gray = morphological_transformation(subject)

        # Take the intersection of the lowest and highest gray values
        intersection_reference = reference_lowest_gray + reference_highest_gray
        intersection_subject = subject_lowest_gray + subject_highest_gray

        # Binarize the images
        binary_reference = binarize_image(intersection_reference)
        binary_subject = binarize_image(intersection_subject)

        binary_subject = cv.dilate(binary_subject, cv.getStructuringElement(cv.MORPH_ELLIPSE, (10, 10)), iterations=1)
        binary_reference = cv.dilate(binary_reference, cv.getStructuringElement(cv.MORPH_ELLIPSE, (10, 10)), iterations=1)

        # Compare the binary images using the euclidean distance
        distance = cv.matchShapes(binary_reference, binary_subject, cv.CONTOURS_MATCH_I1, 0.0)
        distances.append(distance)

    # Find the average distance
    average_distance = sum(distances) / len(distances)
    print("Training average distance: " + str(average_distance))

    labels = []
    predictions = []

    # Test the average distance
    for image_pair_reference in dataset.testing:
        # Load the reference image
        reference = load_image(image_pair_reference.reference.get_image_path())

        labels.append(image_pair_reference.figure_name)

        for image_pair_subject in dataset.testing:
            # Load the subject image
            subject = load_image(image_pair_subject.subject.get_image_path())

            # Perform the morphological transformation
            reference_lowest_gray, reference_highest_gray = morphological_transformation(reference)
            subject_lowest_gray, subject_highest_gray = morphological_transformation(subject)

            # Take the intersection of the lowest and highest gray values
            intersection_reference = reference_lowest_gray + reference_highest_gray
            intersection_subject = subject_lowest_gray + subject_highest_gray

            # Binarize the images
            binary_reference = binarize_image(intersection_reference)
            binary_subject = binarize_image(intersection_subject)

            binary_subject = cv.dilate(binary_subject, cv.getStructuringElement(cv.MORPH_ELLIPSE, (10, 10)), iterations=1)
            binary_reference = cv.dilate(binary_reference, cv.getStructuringElement(cv.MORPH_ELLIPSE, (10, 10)), iterations=1)

            # Compare the binary images using the euclidean distance
            distance = cv.matchShapes(binary_reference, binary_subject, cv.CONTOURS_MATCH_I1, 0.0)
            if distance < (average_distance - .005):
                predictions.append(image_pair_subject.figure_name)
                break

    # Calculate the accuracy
    correct = 0
    for i in range(len(labels)):
        if labels[i] == predictions[i]:
            correct += 1

    accuracy = correct / len(labels)
    print("Accuracy: " + str(accuracy))

    # Calculate the precision
    correct = 0




    # # Show images
    # figure = plt.figure(constrained_layout=True)
    # figure.set_size_inches(10, 16)
    # figure.suptitle("Technique 1")
    # (original, morph, intersection, binary) = figure.subfigures(4, 1, height_ratios=[1, 2, 1, 1])
    #
    # # Original
    # original.suptitle("Original")
    # (original_ref, original_sub) = original.subplots(1, 2)
    # original_ref.imshow(reference, cmap='gray')
    # original_ref.set_title("Reference")
    # original_sub.imshow(subject, cmap='gray')
    # original_sub.set_title("Subject")
    #
    # # Morphological Transformation
    # morph.suptitle("Morphological Transformation")
    # ((morph_ref_low, morph_sub_low), (morph_ref_high, morph_sub_high)) = morph.subplots(2, 2)
    # morph_ref_low.imshow(reference_lowest_gray, cmap='gray')
    # morph_ref_low.set_title("R Lowest Gray")
    # morph_ref_high.imshow(reference_highest_gray, cmap='gray')
    # morph_ref_high.set_title("R Highest Gray")
    # morph_sub_low.imshow(subject_lowest_gray, cmap='gray')
    # morph_sub_low.set_title("S Lowest Gray")
    # morph_sub_high.imshow(subject_highest_gray, cmap='gray')
    # morph_sub_high.set_title("S Highest Gray")
    #
    # # Intersection
    # intersection.suptitle("Intersection")
    # (intersection_ref, intersection_sub) = intersection.subplots(1, 2)
    # intersection_ref.imshow(intersection_reference, cmap='gray')
    # intersection_ref.set_title("Reference")
    # intersection_sub.imshow(intersection_subject, cmap='gray')
    # intersection_sub.set_title("Subject")
    #
    # # Binary
    # binary.suptitle("Binary")
    # (binary_ref, binary_sub) = binary.subplots(1, 2)
    # binary_ref.imshow(binary_reference, cmap='gray')
    # binary_ref.set_title("Reference")
    # binary_sub.imshow(binary_subject, cmap='gray')
    # binary_sub.set_title("Subject")
    #
    # plt.show()


def main(dataset):
    """
    Main method for Anthony's individual components.

    :param dataset: Dataset to use.
    :return: None
    """
    # Technique 1
    technique_1(dataset)
    print("Technique 1 complete")


# Only if this file is run directly
if __name__ == '__main__':
    from main import load_data

    main(load_data())
