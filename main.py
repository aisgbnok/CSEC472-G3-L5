"""
CSEC-472 Bonus Lab 5
Author: Anthony Swierkosz


"""
from os import path

from dataset import Dataset


def main():
    # Load data
    base_path = path.dirname(__file__)
    dataset_path = path.abspath(path.join(base_path, "sd04", "png_txt"))
    dataset = Dataset(dataset_path)


# Only if this file is run directly
if __name__ == '__main__':
    main()
