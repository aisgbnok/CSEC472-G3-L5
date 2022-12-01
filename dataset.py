"""
Author: Anthony Swierkosz

Used for loading the dataset and creating the training and testing sets.
Contains Dataset class along with helper classes and functions.
"""

import os
from enum import Enum

TXT_EXT = '.txt'
PNG_EXT = '.png'


class ImageType(Enum):
    """
    Enum for image types, reference image and subject image.
    """
    REFERENCE = 0
    SUBJECT = 1


class Image:
    """
    A single image, either a reference image or a subject image.
    """

    def __init__(self, image_type, path):
        """
        Initialize the image.

        :param image_type: Reference or subject image.
        :param path: Path to the image excluding the extension.
        """
        self.type = image_type
        self.path = path
        self.gender = None
        self.clss = None
        self.history = None

        self.__load()

    def __load(self):
        """
        Load the image's text data based on the image's path.

        :return: None
        """
        with open(self.path + TXT_EXT, 'r') as file:
            # Read file
            data = file.read()
            data = data.strip().split('\n')

            # Get individualized data
            gender = data[0]
            clss = data[1]
            history = data[2]

            # Clean and set data
            self.gender = gender[gender.find(':') + 1:]
            self.clss = clss[clss.find(':') + 1:]
            self.history = history[history.find(':') + 1:]

    def get_image_path(self):
        """
        Get the image's path.

        :return: Path to the image.
        """
        return self.path + PNG_EXT


class ImagePair:
    """
    An Image Pair is a pair of images, a reference image and a subject image.
    """

    def __init__(self, root, figure_name):
        """
        Initialize the image pair.

        :param root: Root directory of the image pair.
        :param figure_name: Name the images share, generally the number.
        """
        self.figure_name = figure_name
        self.reference = None
        self.subject = None

        self.__generate_pair(root)

    def __generate_pair(self, root):
        """
        Generate a pair of images from the root and figure name.

        :return: None
        """
        # Generate paths
        reference_path = os.path.join(root, 'f' + self.figure_name)
        subject_path = os.path.join(root, 's' + self.figure_name)

        # Create image objects
        self.reference = Image(ImageType.REFERENCE, reference_path)
        self.subject = Image(ImageType.SUBJECT, subject_path)


class Dataset:
    """
    Create a dataset object for holding all the data.
    """

    def __init__(self, root, automatic=False):
        """
        Initialize the dataset.

        :param root: Root directory of the dataset.
        :param automatic: Whether to automatically populate the dataset using the root directory. False by default.
        """
        self.root = root
        self.data = []
        self.training = []
        self.testing = []

        if automatic:
            self.populate_dataset(root)

    def populate_dataset(self, root=None, print_progress=False):
        """
        Loads all the image pairs from the root directory.

        :param root: Path to the root directory. If None, uses the Dataset root directory.
        :param print_progress: Whether to print progress messages. False by default.
        :return: None
        """
        # If no root is given, use the default root
        if root is None:
            root = self.root

        if print_progress:
            print("Loading data...")

        # Generate all the Image Pairs
        for rt, dirs, files in os.walk(root):
            for f_name in files:
                if f_name.startswith('f') and f_name.endswith(PNG_EXT):
                    f_name = f_name[1:-4]  # Remove f/s and .png
                    self.data.append(ImagePair(rt, f_name))

        if print_progress:
            print("Splitting data...")

        # Split the data into training and testing sets
        self.training = self.data[:1500]
        self.testing = self.data[1500:]

        if print_progress:
            print("Done")
