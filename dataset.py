import os

TXT_EXT = '.txt'


class Figure:
    """
    A figure object for holding a single figure's data.
    """

    def __init__(self, path):
        self.path = path
        self.gender = None
        self.clss = None
        self.history = None

        self.__load()

    def __load(self):
        """
        Load the figure's text data from the path.

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


class Dataset:
    """
    Create a dataset object for holding all the data.
    """

    def __init__(self, root):
        self.root = root
        self.data = []

        self.__load_data()
        print("Done")

    def __load_data(self):
        """
        Loads all the figures from the root directory.

        :return: None
        """
        print("Loading data...")
        for rt, dirs, files in os.walk(self.root):
            for f_name in files:
                if f_name.endswith(".png"):
                    self.data.append(Figure(os.path.join(rt, f_name[:-4])))

        print("Done")
