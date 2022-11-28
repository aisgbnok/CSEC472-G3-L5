import os

import numpy
import pandas


class Dataset:

    def __init__(self, root):
        self.root = root
        self.data = []
        self.labels = []

        self.__load_data()
        print("Done")

    def __load_data(self):
        image_paths = []
        text_paths = []
        for rt, dirs, files in os.walk(self.root):
            for f_name in files:
                if f_name.endswith(".png"):
                    image_paths.append(os.path.join(rt, f_name[:-4]))
                elif f_name.endswith(".txt"):
                    text_paths.append(os.path.join(rt, f_name[:-4]))

        if image_paths == text_paths:
            print("Image and text files are matched")
        else:
            print("Image and text files are not matched")
        print("Done")
