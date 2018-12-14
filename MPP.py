import numpy as np
import cv2
import  matplotlib.pyplot as plt
class MPP:
    def __init__(self):
        pass
    def get_boundary_points(self, path):
        im = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
#        imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(im, 127, 255, 0)
        im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        cv2.drawContours(im, contours, -1, (0, 255, 0), 3)
        cv2.imshow("window", im)
        cv2.waitKey()

    def mark_white_black(self, boundary_img):
        pass

mpp = MPP()
points = mpp.get_boundary_points('img.PNG')
# BW_points = mpp.get_BW_points('img.PNG')

