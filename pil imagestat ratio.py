import skimage

import numpy as np 
from PIL import Image, ImageChops, ImageStat  

import glob # Import file paths
import mahotas
import pylab
import random # shuffle array

test = []
train = []
imageDetails_list = []
finalTestCheck = []



def difference(imageA, imageB):
    diff_img = ImageChops.difference(imageA, imageB)
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

    trainlength = len(train)
    print("Number of train images:", trainlength)

    testlength = len(test)
    print("Number of test images:", testlength)


    for everyFinger in train:
        test.append(everyFinger)
        #print()

    newLength = len(test)
   # print("new test Length - ", newLength)

    trainNum = 0
    random.shuffle(test)

    while trainNum < trainlength: # go thru each train item
        testNum = 0
        while testNum < newLength: # go thru each test item
            image1 = train[trainNum]
            image2 = test[testNum]

            valid = difference(image1,image2)
            #print("counter - ", testNum)
            # print("Valid", valid)

            if valid < 0.125: # 0 is more similar
                #Image._show(test[testNum])
                #print("yes")
                test.pop(testNum)
                print("train num: ", trainNum)
                print("test num:  ", testNum)
                testNum=0
                trainNum+=1
                if trainNum == trainlength:
                    break
            else:
                # do next iteration
                testNum += 1
                if (testNum >= len(test)):
                    testNum = 0
                    trainNum += 1
                    break

    print("final length of test - ", len(test))
    numCorrect = 0
    for item in test:
        print("File Name:", item.filename[-12:])
        fingerPrintNum = int(item.filename[-11:-7])
        print("Finger Print Number:", fingerPrintNum)
        if(fingerPrintNum > 1500):
            numCorrect += 1
    print("Number of correct fingerprints: " + str(numCorrect) + "/500")

if __name__ == '__main__':
   main()