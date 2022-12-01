"""
Author: Harsha Philip
"""

import glob  # Import file paths
import random  # shuffle array

from PIL import Image, ImageChops, ImageStat

test = []
train = []
imageDetails_list = []
finalTestCheck = []


def difference(image_a, image_b):
    diff_img = ImageChops.difference(image_a, image_b)
    # Calculate difference as a ratio.
    stat = ImageStat.Stat(diff_img)
    diff_ratio = sum(stat.mean) / (len(stat.mean) * 255)
    return diff_ratio


def main():
    # Add images to testing
    for finger in glob.glob(
            'sd04\png_txt\*'):
        if finger.endswith('.txt'):
            imageDetails_list.append(finger[-12:])
        else:
            im = Image.open(finger)
            finalTestCheck.append(finger[-12:])
            test.append(im)

    # Add images to training
    for finger2 in glob.glob(
            'sd04\png_txt\*'):
        if finger2.endswith('.png'):
            im2 = Image.open(finger2)
            train.append(im2)

    train_length = len(train)
    print("Number of train images:", train_length)

    test_length = len(test)
    print("Number of test images:", test_length)

    for everyFinger in train:
        test.append(everyFinger)
        # print()

    new_length = len(test)
    # print("new test Length - ", new_length)

    train_number = 0
    random.shuffle(test)

    while train_number < train_length:  # go through each train item
        test_number = 0
        while test_number < new_length:  # go through each test item
            image1 = train[train_number]
            image2 = test[test_number]

            valid = difference(image1, image2)
            # print("counter - ", test_number)
            # print("Valid", valid)

            if valid < 0.125:  # 0 is more similar
                # Image._show(test[test_number])
                # print("yes")
                test.pop(test_number)
                print("train num: ", train_number)
                print("test num:  ", test_number)
                test_number = 0
                train_number += 1
                if train_number == train_length:
                    break
            else:
                # do next iteration
                test_number += 1
                if test_number >= len(test):
                    test_number = 0
                    train_number += 1
                    break

    print("final length of test - ", len(test))
    num_correct = 0
    for item in test:
        print("File Name:", item.filename[-12:])
        finger_print_num = int(item.filename[-11:-7])
        print("Finger Print Number:", finger_print_num)
        if finger_print_num > 1500:
            num_correct += 1
    print("Number of correct fingerprints: " + str(num_correct) + "/500")


if __name__ == '__main__':
    main()
