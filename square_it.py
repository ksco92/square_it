# -*- coding: utf-8 -*-

"""Squares horizontal images in the 'originals' folder and returns them to the 'cropped' folder"""

import cv2
import glob
import os

os.chdir(os.path.dirname(__file__))


##########################################
##########################################
##########################################
##########################################


def square_it(file_name):
    pic = cv2.imread(file_name)

    height, width, channels = pic.shape

    crop_pic = pic[0:height, int((width - height) / 2):int(((width - height) / 2) + height)]

    file_name = file_name.split('\\')[1]

    cv2.imwrite('cropped/' + file_name, crop_pic)


if __name__ == '__main__':

    all_pics = glob.glob('originals/*[!.modd]')

    for picture in all_pics:
        square_it(picture)
