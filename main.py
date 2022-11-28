"""
CSEC-472 Bonus Lab 5
Author: Anthony Swierkosz


"""
from os import path

from dataset import Dataset


# def load_data(root):
#
#     x = []
#     y = []
#
#     # Create paths and do instance count filtering
#     for rt, dirs, files in os.walk(root):
#         for f_name in files:
#             path = os.path.join(rt, f_name)
#             label = os.path.basename(os.path.dirname(path))


def main():
    # Load data
    base_path = path.dirname(__file__)
    dataset_path = path.abspath(path.join(base_path, "sd04", "png_txt"))
    dataset = Dataset(dataset_path)
    print("Hello World")


# Only if this file is run directly
if __name__ == '__main__':
    main()
