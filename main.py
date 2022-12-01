"""
CSEC-472 Bonus Lab 5
Author: Anthony Swierkosz

Main program for the bonus lab.
Brings everything together and lets you run selected components.
"""
from enum import Enum
from os import path
from textwrap import wrap

from dataset import Dataset


class MenuStyle(Enum):
    """
    Enum for the menu style.
    """
    FULL = 0
    WELCOME = 1
    MENU = 2
    EXIT = 3


def bold(text):
    """
    Return the text in bold.

    :param text: Text to bold.
    :return: Bolded text.
    """
    return f"\033[1m{text}\033[0m"


def print_menu(style=MenuStyle.MENU):
    """
    Print the welcome message.

    :return: Integer of user choice if style is FULL or MENU, otherwise None.
    """
    title = "CSEC 472: Lab 5"
    subtitle = "Group 3"
    width = len(title) + 24 if len(title) > len(subtitle) else len(subtitle) + 24
    # description = " ##\n## ".join(wrap("Choose one of the options below to run a component of the lab.", width - 4))
    description = "\n".join(wrap("Choose one of the options below to run a component of the lab.", width))

    if style == MenuStyle.FULL or style == MenuStyle.WELCOME:
        print(f'{"":#^{width}}')
        print(f'##{f" {bold(title)} ":^{width + 4}}##')
        print(f'##{f" {subtitle} ":^{width - 4}}##')
        print(f'{"":#^{width}}\n')

    if style == MenuStyle.FULL or style == MenuStyle.MENU:
        print(f'{"## User Menu ":#<{width}}')
        print(f'{description}\n')

        print("0. Exit")
        print("1. Run Anthony's individual components.")
        print("2. Run Harsha's individual components.")

        user_choice = int(input("\nEnter your choice: ").strip())
        print(f'{"":#^{width}}\n')

        return user_choice

    if style == MenuStyle.EXIT:
        print(f'{"## Exiting Program ":#<{width}}')
        print(f'##{" Thank you, for enduring our ":<{width - 4}}##')
        print(f'##{" lackluster results! :( ":<{width - 4}}##')
        print(f'{"":#^{width}}\n')


def load_data():
    """
    Load the dataset into a Dataset object.

    :return: None
    """
    # Get the path to the dataset
    base_path = path.dirname(__file__)
    dataset_path = path.abspath(path.join(base_path, "sd04", "png_txt"))

    # Load the dataset
    print("## Generating the Dataset")
    dataset = Dataset(dataset_path)
    dataset.populate_dataset(print_progress=True)
    print()
    return dataset


def main():
    print_menu(MenuStyle.WELCOME)

    # Load Dataset
    dataset = load_data()

    # Handle user menu selection
    user_choice = -1
    while user_choice != 0:
        user_choice = print_menu()

        if user_choice == 1:
            from anthony_individual import main as anthony_main
            anthony_main(dataset)

        elif user_choice == 2:
            print("Harsha's individual components are not automatic at this time.")
            print("Instead you can run percent_stddev.py, pil imagestat ratio.py, and rms.py, separately.")
            print("They all have Harsha's name as the author.")
            print("Results are found in the respective .txt files.")
            print("Thank you!")

        print()

    print_menu(MenuStyle.EXIT)


# Only if this file is run directly
if __name__ == '__main__':
    main()
