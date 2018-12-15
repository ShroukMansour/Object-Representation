import numpy as np
import cv2
from Point import Point
import  matplotlib.pyplot as plt
class MPP:
    def __init__(self):
        pass

    def get_boundary_points(self, path):
        im = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        ret, thresh = cv2.threshold(im, 127, 255, 0)
        im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        boundary = np.reshape(contours[0], [contours[0].shape[0], contours[0].shape[2]])
        # cv2.drawContours(im, contours, -1, (0, 255, 0), 3)
        # cv2.imshow("window", im)
        # cv2.waitKey()
        return boundary

    def get_BW_points(self, path, w, h):
        boundary = self.get_boundary_points(path)
        bw_points = [Point(boundary[0])]
        for i in range(1, boundary.shape[0]-1, w):
            p = Point(boundary[i])
            type = p.calc_type(boundary[i-1], boundary[i+1])
            if type != 0:
                bw_points.append(p)
        return np.array(bw_points)

mpp = MPP()
# returns an array of points, make sure it's clockwise or anticlock wise as you need
BW_points = mpp.get_BW_points('img2.png', 2, 2)
print(BW_points.shape)

